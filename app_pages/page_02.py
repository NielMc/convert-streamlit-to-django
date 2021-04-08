import streamlit as st
from config import config
from src.processing.data_management import TrainTestSplit

def BodyPage2(df):
    
    # ### Page 2: ML model
    # * Button to fit and save a ML model. Once finished, the model is evaluated on train and test set.
    st.write("#### Clf1_BR2")
    
    X_train, X_test,y_train, y_test = TrainTestSplit(df=df,TARGET=config.TARGET_Clf1_BR2)
    
    # check if there is model
    # if not
        # split, fit, save  train set, test set, model
    # else 
        # load saved train,test, and model
    
    # evaluate model
    
    