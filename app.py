from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig , DataTransformation
from src.mlproject.components.model_trainer import ModelTrainerConfig , ModelTrainer
import sys
if __name__ == "__main__":
    logging.info("Logging has Successfully Started")

    try:
        data_ingestion = DataIngestion()
        train_data_path , test_data_path = data_ingestion.initiate_data_ingestion()

        data_tranformation = DataTransformation()
        train_arr , test_arr ,_= data_tranformation.initiate_data_transormation(train_data_path , test_data_path)


        ## Model Traning

        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr , test_arr))


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e , sys)

