import streamlit as st
from src.processing.eda import PlotPairplot, Plot3D, HeatmapCorrelation
from config import config

def DataVisualizationBody(df):

    st.write("---")
    st.write("#### Pair Plot")
    PlotPairplot(df,config.TARGET_Clf1_BR2)

    st.write("---")
    st.write("#### 3D Plot")
    Plot3D(df,config.TARGET_Clf1_BR2)

    st.write("---")
    st.write("#### Correlation Heatmap")
    HeatmapCorrelation(df)