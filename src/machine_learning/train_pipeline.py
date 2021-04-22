import numpy as np
import pandas as pd
from config import config
import streamlit as st


import src.machine_learning.pipeline as pipeline
from src.processing.data_management import SavePipeline,SaveTrainTestSets



def TrainPipeline_ClfIrisSpecies(X_train, X_test, y_train, y_test) -> None:
    
    # load raw-pipeline
    ml_pipeline = pipeline.ClfIrisSpecies_DT    
    
    ml_pipeline.fit(X_train,y_train)
    
    SavePipeline(pipeline_to_save=ml_pipeline, model_name=config.ClfIrisSpecies_NAME)
    
    SaveTrainTestSets(
        model_name=config.ClfIrisSpecies_NAME,
        target=config.ClfIrisSpecies_TARGET,
        X_train=X_train, X_test=X_test,
        y_train=y_train, y_test=y_test
    )
    
    return ml_pipeline