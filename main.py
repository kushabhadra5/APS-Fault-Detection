from sensor.pipeline.training_pipeline import initiate_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction

file_path = "/config/workspace/aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
     try:
          #initiate_training_pipeline()
          start_batch_prediction(input_file_path=file_path)

     except Exception as e:
          print(e)