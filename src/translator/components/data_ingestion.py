import os
import datasets 
from src.translator.logging import logger
from src.translator.utils.common import get_size
from pathlib import Path
from src.translator.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.source):
            logger.info("Downloading data")
            # Load the dataset
            dataset = datasets.load_dataset(f'{self.config.source}')
            
            # Save the dataset to the specified folder
            dataset.save_to_disk(self.config.root_dir)

            logger.info("Dataset ingestion succesful")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.source))}")


