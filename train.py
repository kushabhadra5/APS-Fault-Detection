from sensor.pipeline.training_pipeline import initiate_training_pipeline


file_path="/config/workspace/aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
    try:
        initiate_training_pipeline()
    except Exception as e:
        print(e)