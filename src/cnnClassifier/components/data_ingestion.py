import os
import kagglehub
import shutil
import pandas as pd
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = kagglehub.dataset_download(dataset_url)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            source_dir = os.path.join(zip_download_dir,'survey.csv')
            destination_dir = os.path.join(self.config.local_data_file,'survey.csv')
            
            shutil.copy(source_dir, destination_dir)
            logger.info(f"Copying data from {source_dir} into file {destination_dir}")

        except Exception as e:
            raise e
        
    def read_file(self):
        path = os.path.join(self.config.local_data_file, 'survey.csv')
        try:
            df = pd.read_csv(path)
            return df
        except Exception as e:
            raise e