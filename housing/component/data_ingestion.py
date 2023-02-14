from housing.exception import HousingException
import os, sys


class DataIngestion:
    def __init__(self, data_ingestion_config) -> None:
          try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
 
        
         except Exception as e:
            raise HousingException(e,sys) from e