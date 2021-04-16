import streamlit as st
from config import config
import os

import __init__
_version = __init__.__version__

from src.processing.data_management import TrainTestSplit, LoadPipeline, LoadTrainTestSets
from src.machine_learning.train_pipeline import TrainPipeline_ClfIrisSpecies
from src.machine_learning.model_evaluation import ClfEvaluation

def ML_ClfIrisSpeciesBody(df):
    
    st.write("## ClfIrisSpecies")
    st.write("---")
    

    # Check if model was already trained/save
    list_saved_models = os.listdir(config.PACKAGE_ROOT / config.TRAINED_MODEL_DIR)
    list_saved_models = [item.split('.')[0] for item in list_saved_models] 
    desired_file_pattern = f"{config.ClfIrisSpecies_NAME}_v{_version}"
    
    if desired_file_pattern not in list_saved_models:
        X_train, X_test,y_train, y_test = TrainTestSplit(
                                                        df=df,
                                                        TARGET=config.ClfIrisSpecies_TARGET)
        pipeline_ClfIrisSpecies = TrainPipeline_ClfIrisSpecies(X_train, X_test, y_train, y_test)
        
    
    else:
        pipeline_ClfIrisSpecies = LoadPipeline(model_name=config.ClfIrisSpecies_NAME)
        X_train, X_test, y_train, y_test = LoadTrainTestSets(model_name=config.ClfIrisSpecies_NAME)
    
    
    # pipeline steps
    st.write("### ML Pipeline Steps")
    st.write(pipeline_ClfIrisSpecies.steps) 

    
    ## Main Features
    st.write(
        "### Main Features",
        X_train.columns[pipeline_ClfIrisSpecies['feat_selection'].get_support()].to_list()
    )
    
      
    # Model Evaluation
    st.write("### Evaluation on Train Set")
    ClfEvaluation(
        Prediction=pipeline_ClfIrisSpecies.predict(X_train),
        Actual=y_train
    )
    
    
    st.write("### Evaluation on Test Set")
    ClfEvaluation(
        Prediction=pipeline_ClfIrisSpecies.predict(X_test),
        Actual=y_test
    )
    
    
    