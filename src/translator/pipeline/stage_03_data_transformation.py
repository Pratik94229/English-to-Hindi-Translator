from src.translator.config.configuration import ConfigurationManager
from src.translator.components.data_transformation import DataTransformation
from datasets import load_dataset, load_from_disk
from src.translator.logging import logger
from transformers import AutoTokenizer



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            raw_dataset = load_from_disk(data_transformation_config.data_path)
            logger.info("Data loaded from disk")
    
            tokenized_datasets = raw_dataset.map(data_transformation.preprocess_function, batched=True)

            # Save tokenized datasets to the specified directory
            data_transformation.save_tokenized_datasets(tokenized_datasets)
    
        except Exception as e:
            raise e
      
        