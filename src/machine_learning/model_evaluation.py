import streamlit as st
import pandas as pd
from config import config

def ClfEvaluation(Prediction, Actual):

    from sklearn.metrics import classification_report,confusion_matrix  

    st.write("#### Classification Report")
    st.code(classification_report(Actual, Prediction))

    st.write("#### Confusion Matrix")
    ClassMap = config.Clf1_BR2_Map.values()

    st.code(pd.DataFrame(confusion_matrix(Prediction,Actual),
                columns=[ ["Actual " + sub for sub in ClassMap] ], 
                index = [ ["Prediction " + sub for sub in ClassMap ]]
                # index=['Prediction 0', 'Prediction 1']
                ))
    
    st.write("---")