#Import required dependencies and packages
import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
from sensor.config import mongo_client


#Configure the data:
Dat_File_Path = "/config/workspace/aps_failure_training_set1.csv"
Database_Name = 'aps'
Collection_Name = 'sensor'

if __name__ == "__main__":
    #Loading the data as dataframe
    df = pd.read_csv(Dat_File_Path)
    #Checking the loaded data
    print("Rows and Columns: ", df.shape)

    #Before dumping the data to MongoDB we will reset the index of the data
    df.reset_index(drop = True, inplace = True)

    #First, for json format we need to change the format of our dataframe that is we'll be using transpose of the dataframe
    #Second, the converted data is a valid JSON string that will get converted into Python dictionary.
    #Third, accumulate all the dictionaries into list.
    json_record = list(json.loads(df.T.to_json()).values())

    #Inserting the data to MongoDB
    mongo_client[Database_Name][Collection_Name].insert_many(json_record)
    print("\nData successfully uploaded to MongoDB.")