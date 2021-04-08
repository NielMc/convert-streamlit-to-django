import streamlit as st
from app_pages.page_01 import BodyPage1
from app_pages.page_02 import BodyPage2
from app_pages.page_03 import BodyPage3
from src.data_management import LoadIrisDataset

from config import config
import __init__
_version = __init__.__version__
# st.write(config.PACKAGE_ROOT, _version)

def main():

    df = LoadIrisDataset()

    MenuOptions = [
        'EDA',
        'ML Model',
        'User Interface',
        ]
    page = st.sidebar.radio("Main Menu",MenuOptions,index=0)
    
    if page == MenuOptions[0]: BodyPage1(df)
    elif page == MenuOptions[1]: BodyPage2(df)   
    elif page == MenuOptions[2]: BodyPage3(df)

if __name__ == '__main__': main()