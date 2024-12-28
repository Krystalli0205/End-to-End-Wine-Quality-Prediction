import pandas as pd
import os
from wine_quality_prediction_project import logger
from sklearn.model_selection import train_test_split
from wine_quality_prediction_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # here only use train_test_split as an example, bcz the data is clean
    # make changes to this code later when i add more details (like EDA, feature engineering etc) to the model
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        
        # 0.75 train, 0.25 test split
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Splitted data into train and test and saved in {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(f"train shape: {train.shape}")
        print(f"test shape: {test.shape}")