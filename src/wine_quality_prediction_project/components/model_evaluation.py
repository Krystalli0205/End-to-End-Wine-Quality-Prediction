import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import joblib # to load the model
from pathlib import Path
from urllib.parse import urlparse 
from wine_quality_prediction_project.utils.common import save_json
from wine_quality_prediction_project.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual_values, predicted_values):
        rmse = np.sqrt(mean_squared_error(actual_values, predicted_values))
        mae = mean_absolute_error(actual_values, predicted_values)
        r2 = r2_score(actual_values, predicted_values)
        return rmse, mae, r2
    
    def save_results(self):
        # load test data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        # get test x and test y
        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]
        
        # get predictions
        predictions = model.predict(test_x)
        
        # get metrics
        rmse, mae, r2 = self.eval_metrics(test_y, predictions)
        
        # save metrics
        result = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        save_json(path=Path(self.config.metric_file_name), data=result) # in utils.common has been defined ("save_json")
        
        
        