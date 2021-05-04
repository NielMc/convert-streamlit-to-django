import streamlit as st
from config import config
from src.processing.data_management import LoadPipeline
from src.processing.user_interface import CreateWidgetsUI

def ML_UI_Body(df):
    
    st.write("## Machine Learning UI")
    st.write("---")
    
    X_live = CreateWidgetsUI(df)
    
    pipeline_ClfIrisSpecies = LoadPipeline(
                                    model_name="ClfModel",
                                    path="outputs/trained_models")
    st.write("---")
    
    if st.button("Predict"):
        
        
        y_live = int(pipeline_ClfIrisSpecies.predict(X_live))
        y_liveProba = pipeline_ClfIrisSpecies.predict_proba(X_live)

        ProbText = ""
        for x in range(0,len(y_liveProba[0])):
            aux = f"	* {config.ClfIrisSpecies_MAP[x]}: {round(y_liveProba[0][x],2)} \n "
            ProbText = ProbText + aux

        st.info(
            f"* The predicted class is **{config.ClfIrisSpecies_MAP[y_live]}** \n"
            f"* The probability for each class is: \n\n "
            f"{ProbText}")
        

       
