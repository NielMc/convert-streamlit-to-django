import streamlit as st
from config import config


from src.processing.data_management import TrainTestSplit, LoadPipeline, LoadTrainTestSets
from src.machine_learning.model_evaluation import ClfEvaluation

def ML_ClfIrisSpeciesBody(df):
    
    st.write("## ClfIrisSpecies")
    st.write("---")
    
    pipeline_ClfIrisSpecies = LoadPipeline(
                                    model_name="ClfModel",
                                    path="outputs/trained_models")

    X_train, X_test, y_train, y_test = LoadTrainTestSets(
                                                    model_name="ClfModel",
                                                    path="outputs/datasets")
    
    
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
    
    
    