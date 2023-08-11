import os
import sys
import transformers
import tensorflow as tf
from datasets import load_dataset,load_from_disk
from transformers import AutoTokenizer
from transformers import TFAutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from transformers import AdamWeightDecay
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from src.translator.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        tokenized_datasets=load_from_disk(self.config.data_path)
        
        model = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, return_tensors="tf")
        generation_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, return_tensors="tf", pad_to_multiple_of=128)
        

        #Since my machine is not very powerful so i am training with test data but while predicting using api I will try to incorporate
        # model trained from google collab.  

        train_dataset = model.prepare_tf_dataset(
            tokenized_datasets["test"],
            batch_size=self.config.batch_size,
            shuffle=True,collate_fn=data_collator)
        

        validation_dataset = model.prepare_tf_dataset(
        tokenized_datasets["validation"],
        batch_size=self.config.batch_size,
        shuffle=False,
        collate_fn=data_collator,)

        generation_dataset = model.prepare_tf_dataset(
        tokenized_datasets["validation"],
        batch_size=8,
        shuffle=False,
        collate_fn=generation_data_collator,
)
      
        optimizer = AdamWeightDecay(learning_rate=self.config.learning_rate, weight_decay_rate=self.config.weight_decay)
        model.compile(optimizer=optimizer)
        model.fit(train_dataset, validation_data=validation_dataset, epochs=1)
        

        model.save_pretrained(self.config.root_dir)
