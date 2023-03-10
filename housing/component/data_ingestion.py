from housing.exception import HousingException
import os, sys
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.logger import logging
import tarfile
from six.moves import urllib
from housing.config.configuration import DataIngestionConfig



class DataIngestion:
   def __init__(self, data_ingestion_config) -> None:
      try:
         logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
         self.data_ingestion_config = data_ingestion_config
 
        
      except Exception as e:
         raise HousingException(e,sys) from e

   def download_housing_data(self):
      download_url=self.data_ingestion_config.dataset_download_url
      tgz_download_dir=self.data_ingestion_config.tgz_download_dir

      if os.path.exists(tgz_download_dir):
         os.remove(tgz_download_dir)

      os.makedirs(tgz_download_dir,exist_ok=True)
      housing_file_name=os.path.basename(download_url)

      tgz_file_path=os.path.join(tgz_download_dir,housing_file_name)
      logging.info(f"Downloading file from:[{download_url}] into :[{tgz_file_path}]")

      urllib.request.urlretrieve(download_url,tgz_file_path)

      logging.info(f"File:[{tgz_file_path}] has been downloaded successfully")
      return tgz_file_path


   def extract_tgz_file(self):
      raw_data_dir=self.data_ingestion_config.raw_data_dir

      

   def split_data_as_train_test(self):
      pass      

   def initiate_data_ingestion(self) ->DataIngestionArtifact:
      try:
         tgz_file_path=self.download_housing_data()
      except Exception as e:
         raise HousingException(e,sys) from e


