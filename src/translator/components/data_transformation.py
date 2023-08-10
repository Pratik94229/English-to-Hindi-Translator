import os
from transformers import AutoTokenizer
from datasets import load_dataset
from src.translator.entity import DataTransformationConfig
from src.translator.logging import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        self.source = config.source
        self.save_dir = config.root_dir
        

    def preprocess_function(self,examples):
        max_input_length = 128
        max_target_length = 128

        source_lang = "en"
        target_lang = "hi"
        inputs = [ex[source_lang] for ex in examples["translation"]]
        targets = [ex[target_lang] for ex in examples["translation"]]
        model_inputs = self.tokenizer(inputs, max_length=max_input_length, truncation=True)

        # Setup the tokenizer for targets
        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(targets, max_length=max_target_length, truncation=True)

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    def save_tokenized_datasets(self, tokenized_datasets):
        os.makedirs(self.save_dir, exist_ok=True)
        tokenized_datasets.save_to_disk(self.save_dir)





