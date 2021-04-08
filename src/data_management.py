import pandas as pd
import streamlit as st

def LoadIrisDataset():
    from sklearn.datasets import load_iris
    
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["Species"] = pd.Series(data.target)

    return df