import streamlit as st
from src.processing.eda import PlotPairplot, Plot3D
from config import config

def DataVisualizationBody(df):
    
    st.write("## Data Visualization")
    st.write("---")
    
    st.write("#### Pair Plot")
    PlotPairplot(df,config.ClfIrisSpecies_TARGET)

    st.write("---")
    st.write("#### 3D Plot")
    Plot3D(df,config.ClfIrisSpecies_TARGET)

