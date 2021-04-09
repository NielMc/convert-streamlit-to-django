import streamlit as st
from config import config
from src.processing.data_management import LoadPipeline

def ML_UI_Body(df):
    
    st.write("## Machine Learning UI")
    st.write("---")
    
    X_live = CreateWidgetsUI(df)
    
    pipeline_ClfIrisSpecies = LoadPipeline(model_name=config.ClfIrisSpecies_NAME)
    st.write("---")
    
    if st.button("Predict"):
        
        
        y_live = int(pipeline_ClfIrisSpecies.predict(X_live))
        y_liveProba = pipeline_ClfIrisSpecies.predict_proba(X_live)

        ProbText = ""
        for x in range(0,len(y_liveProba[0])):
            aux = f"	* {config.ClfIrisSpecies_MAP[x]}: {round(y_liveProba[0][x],2)} \n "
            ProbText = ProbText + aux

        st.info(
            f"* The predicted class is **{(y_live)}: {config.ClfIrisSpecies_MAP[y_live]}** \n"
            f"* The probability for each class is: \n\n "
            f"{ProbText}")

       

    
def CreateWidgetsUI(df):
    import pandas as pd
    
    col1, col2, = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)
    
    percentageMin,percentageMax = 0.8 , 1.2
    step = 0.05
    
    with col1:
        feature = 'sepal length (cm)'
        sepal_length = st.slider(
            'Enter sepal_length',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col2:
        feature = 'sepal width (cm)'
        sepal_width = st.slider(
            'Enter sepal_width',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col3:
        feature = 'petal length (cm)'
        petal_length = st.slider(
            'Enter petal_length',
            min_value=float(df[feature].min() * percentageMin),
            max_value=float(df[feature].max() * percentageMax),
            step=step,
            value=float(df[feature].median())
        )
    
    with col4:
        feature = 'petal width (cm)'
        petal_width = st.slider(
            'Enter petal_width',
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