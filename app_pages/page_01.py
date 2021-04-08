import streamlit as st
from src.eda import PlotPairplot, Plot3D, HeatmapCorrelation
from config import config

def BodyPage1(df):

    st.write("---")
    st.write("#### Pair Plot")
    PlotPairplot(df,"Species")

    st.write("---")
    st.write("#### 3D Plot")
    Plot3D(df,"Species")

    st.write("---")
    st.write("#### Correlation Heatmap")
    HeatmapCorrelation(df)