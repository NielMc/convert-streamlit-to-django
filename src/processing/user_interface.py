import streamlit as st
import pandas as pd


def CreateWidgetsUI(df):
    
    
    col1, col2, = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)
    
    percentageMin,percentageMax = 0.8 , 1.2
    step = 0.05
    
    with col1:
        feature = 'sepal length (cm)'
        sepal_length = st.slider(
            'Enter sepal length',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col2:
        feature = 'sepal width (cm)'
        sepal_width = st.slider(
            'Enter sepal width',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col3:
        feature = 'petal length (cm)'
        petal_length = st.slider(
            'Enter petal length',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col4:
        feature = 'petal width (cm)'
        petal_width = st.slider(
            'Enter petal width',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
        
    X_live = pd.DataFrame(
		data={
            df.columns[0]: sepal_length,
            df.columns[1]: sepal_width,
            df.columns[2]: petal_length,
            df.columns[3]: petal_width
            },
		index=[0]
    )
    

    return X_live