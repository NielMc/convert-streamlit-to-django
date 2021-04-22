import streamlit as st
from app_pages.page_ml_ui import ML_UI_Body
from app_pages.page_data_visualization import DataVisualizationBody
from app_pages.page_ml_ClfIrisSpecies import ML_ClfIrisSpeciesBody
from src.processing.data_management import LoadIrisDataset

from config import config
_version = config.version_model
## st.write("* Model version: ",_version, "\n", "* App root folder: ",config.PACKAGE_ROOT)


def main():

    df = LoadIrisDataset()

    MenuOptions = [
        'User Interface',
        'Data Visualization',
        'ML Model: ClfIrisSpecies'
        ]
    page = st.sidebar.radio("Main Menu",MenuOptions,index=0)
    
    if page == MenuOptions[0]: ML_UI_Body(df)
    elif page == MenuOptions[1]: DataVisualizationBody(df)   
    elif page == MenuOptions[2]: ML_ClfIrisSpeciesBody(df)

if __name__ == '__main__': main()