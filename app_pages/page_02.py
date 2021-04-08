import streamlit as st
from config import config

from src.processing.data_management import TrainTestSplit
from src.machine_learning.train_pipeline import TrainPipeline_Clf1_BR2

def BodyPage2(df):
    
    st.write("#### Clf1_BR2")
    
    if True:
        X_train, X_test,y_train, y_test = TrainTestSplit(df=df,TARGET=config.TARGET_Clf1_BR2)
        pipeline_Clf1_BR2 = TrainPipeline_Clf1_BR2(X_train, X_test, y_train, y_test)
        st.write(pipeline_Clf1_BR2)
    else:
        st.write("load saved train,test set and model")
    
    
      
    # evaluate model
    
    