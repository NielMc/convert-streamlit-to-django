import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from config import config

def PlotPairplot(dfRaw,TARGET):
    
    df = dfRaw.copy()
    df[TARGET] = df[TARGET].replace(config.ClfIrisSpecies_MAP)
    
    fig = sns.pairplot(
        data=df,
        hue= TARGET,
        plot_kws={'alpha':0.8},
        )
    for i, j in zip(*np.triu_indices_from(fig.axes, 1)):
        fig.axes[i, j].set_visible(False)
    st.pyplot(fig)




def Plot3D(df_original,TARGET):

    FeaturesColumns = df_original.drop([TARGET],axis=1).columns

    col1, col2, col3 = st.beta_columns(3)
    with col1: select_x = st.selectbox(label="Select X", options=FeaturesColumns,index=0)
    with col2: select_y = st.selectbox(label="Select Y", options=FeaturesColumns,index=1)
    with col3: select_z = st.selectbox(label="Select Z", options=FeaturesColumns,index=2)


    df = df_original.copy()
    df[TARGET] = df[TARGET].replace(config.ClfIrisSpecies_MAP)
    df[TARGET] = df[TARGET].astype(str)
    
    fig = px.scatter_3d(df, x=select_x, y=select_y, z=select_z,
        color=TARGET, 
        size_max=12,
        opacity=0.8,
        width=800,
        height=700,
        color_discrete_sequence=px.colors.qualitative.Light24)


    st.plotly_chart(fig)


