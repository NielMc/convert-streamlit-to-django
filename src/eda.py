import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

def PlotPairplot(df,TARGET):
    

    # FeaturesColumns = df_original.drop([TARGET],axis=1).columns
    # pairplot_columns = st.multiselect(label="Select Features", options=FeaturesColumns)


    # df = df_original.copy().filter(pairplot_columns + [TARGET])

    # if len(df.columns) > 2:
    fig = sns.pairplot(
        data=df,
        hue= TARGET,
        plot_kws={'alpha':0.8},
        # palette=sns.color_palette("RdBu_r", 7)
        )
    for i, j in zip(*np.triu_indices_from(fig.axes, 1)):
        fig.axes[i, j].set_visible(False)
    st.pyplot(fig)#,clear_figure=True)




def Plot3D(df_original,TARGET):

    FeaturesColumns = df_original.drop([TARGET],axis=1).columns

    col1, col2, col3 = st.beta_columns(3)
    with col1: select_x = st.selectbox(label="Select X", options=FeaturesColumns,index=0)
    with col2: select_y = st.selectbox(label="Select Y", options=FeaturesColumns,index=1)
    with col3: select_z = st.selectbox(label="Select Z", options=FeaturesColumns,index=2)


    df = df_original.copy()
    df[TARGET] = df[TARGET].astype(str)
    fig = px.scatter_3d(df, x=select_x, y=select_y, z=select_z,
        color=TARGET, 
        size_max=12,
        opacity=0.8,
        width=800,
        height=700,
        color_discrete_sequence=px.colors.qualitative.Light24)


    st.plotly_chart(fig)



def HeatmapCorrelation(df):

    col1, col2 = st.beta_columns(2)

    with col1: CorrType = st.selectbox(label="Select Correlation Type", options=['spearman','pearson'])
    with col2: CorrThreshold = st.selectbox(label="Select Threshold Level", options=[0,0.4,0.6])
    

    
    df_corr = df.corr(method=CorrType)
    NumberOfColumns = len(df.columns)

    
    if NumberOfColumns > 1:
        mask = np.zeros_like(df_corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df_corr) < CorrThreshold] = True

        fig, ax = plt.subplots()
        ax = sns.heatmap(
            df_corr,
            annot=True,
            xticklabels=True,
            yticklabels=True,
            mask=mask,
            cmap='viridis',
            annot_kws={"size": 8})

        plt.ylim(NumberOfColumns,0)
        st.pyplot(fig,clear_figure=True)