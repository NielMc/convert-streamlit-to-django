import streamlit as st
from config import config
from src.processing.data_management import LoadPipeline

def ML_UI_Body(df):
    #* User Interface with inputs (flower measurements) as numerical fields 
    # #and prediction as a statement
    
    st.write(df.columns)
    
    X_live = CreateWidgetsUI(df)
    
    pipeline_ClfIrisSpecies = LoadPipeline(model_name=config.ClfIrisSpecies_NAME)
    
    if st.button("Predict"):
    
        Prediction_live = pipeline_ClfIrisSpecies.predict(X_live)[0]
        Prediction_label = config.ClfIrisSpecies_MAP[Prediction_live]
        st.write(
            f"* There is xx% of probability to be a **{Prediction_label}** species."
            )


    
def CreateWidgetsUI(df):
    import pandas as pd
    
    col1, col2, col3, col4 = st.beta_columns(4)
    percentageMin,percentageMax = 0.8 , 1.2
    
    with col1:
        feature = 'sepal length (cm)'
        sepal_length = st.number_input(
            'Enter sepal_length',
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    
    with col2:
        feature = 'sepal width (cm)'
        sepal_width = st.number_input(
            'Enter sepal_width',
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    
    with col3:
        feature = 'petal length (cm)'
        petal_length = st.number_input(
            'Enter petal_length',
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    
    with col4:
        feature = 'petal width (cm)'
        petal_width = st.number_input(
            'Enter petal_width',
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
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