import os
import datasets
import pandas as pd
from src.translator.logging import logger
from src.translator.utils.common import get_size
from pathlib import Path
from src.translator.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading data")
            dataset = datasets.load_dataset(f'{self.config.source}')

            # Step 2: Convert the dataset to a Pandas DataFrame
            df_train = pd.DataFrame(dataset["train"])
            df_test = pd.DataFrame(dataset["test"])
            df_validation= pd.DataFrame(dataset["validation"])
            
            # Save the DataFrame to a CSV file in the desired folder
            df_train.to_csv(self.config.root_dir + "/train.csv", index=False)
            df_validation.to_csv(self.config.root_dir + "/validation.csv", index=False)
            df_test.to_csv(self.config.root_dir + "/test.csv", index=False)
            
            logger.info("Dataset ingestion succesful")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        

