import numpy as np
import pandas as pd
from config import config
import streamlit as st


import src.machine_learning.pipeline as pipeline
from src.processing.data_management import SavePipeline,SaveTrainTestSets

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
 

def TrainPipeline_Clf1_BR2(X_train, X_test, y_train, y_test) -> None:
    
    
    ml_pipeline = pipeline.Clf1_BR2  # load raw-pipeline
    
    # set grid search
    
    
    ml_pipeline.fit(X_train,y_train)
    
    SavePipeline(pipeline_to_persist=ml_pipeline, model_name=config.Clf1_BR2_name)
    
    SaveTrainTestSets(
        model_name=config.Clf1_BR2_name,
        target=config.TARGET_Clf1_BR2,
        X_train=X_train, X_test=X_test,
        y_train=y_train, y_test=y_test
    )
    
    return ml_pipeline