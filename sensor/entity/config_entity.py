#This file will defines input for each components
#Here the enities are the components of training pipeline

import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

#Name and format of the file to be created in DataIngestion component
FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        '''In the current directory this will create a folder name artifact with timestamp'''
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise SensorException(e,sys)     


class DataIngestionConfig:
    '''This will use the above TrainingPipelineConfig artifact directly'''
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            #In the previously created artifact directory, creating new directory data_ingestion
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            #In the above created data_ingestion directory two folders will be created:
            #1. feature_store folder that will contain sensor data with name (sensor.csv)
            #2. dataset folder that will contain our training data with name (train.csv) and our test data with name (test.csv)
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise SensorException(e,sys)     

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise SensorException(e,sys)


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...