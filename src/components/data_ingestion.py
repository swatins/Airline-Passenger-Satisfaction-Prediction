import os, sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig
#from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw_data.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try :
            cdf= pd.read_csv(os.path.join('notebook\data',"Passenger_raw_dataset.csv"))            
            logging.info("Read the dataset as dataframe")
            
            cdf.columns = [c.replace(' ', '_') for c in cdf.columns]
            #cdf=cdf.rename(columns={"On-board_service": "On_board_service"})
            logging.info("Changing column names in  DF is done ")
            df=cdf
            #logging.info(f"("changed col names are {df.columns}")
            print(df.columns)
           
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header =True)
            
            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header =True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header =True)
            
            logging.info("Data Ingestion is done")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error occured in data ingestion stage")
            raise CustomException(e,sys)
        
if __name__== "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    
    # src\components\data_ingestion.py