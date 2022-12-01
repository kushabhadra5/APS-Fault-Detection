import pandas as pd
from sensor.config import mongo_client
from sensor.exception import SensorException
from sensor.logger import logging


def get_collection_as_dataframe(database_name:str , collection_name:str)->pd.DataFrame:
    '''This function will collect all the documents present in the MongoDB,
    then convert it to a list and then converted into a dataframe.'''
    try:
        logging.info(f"Loading data from database: {database_name}  and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Found _id column while loading from MongoDB, so dropping the\
                id column from the data frame.")
            df = df.drop("_id", axis = 1)
        return df
    
    except Exception as e:
        raise SensorException(e, sys)