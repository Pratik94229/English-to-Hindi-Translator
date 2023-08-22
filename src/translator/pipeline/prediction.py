import os
from transformers import AutoTokenizer
from src.translator.logging import logger
from src.translator.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM


# prediction.py
class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_prediction_config()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        self.model = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

    def predict(self, text):
        tokenized = self.tokenizer([text], return_tensors='np')
        out = self.model.generate(**tokenized, max_length=128)

        with self.tokenizer.as_target_tokenizer():
            return self.tokenizer.decode(out[0], skip_special_tokens=True)
        
try:
    config = ConfigurationManager()
    model_prediction_config = config.get_model_prediction_config()
    model_predict = PredictionPipeline()
except Exception as e:
    raise e
