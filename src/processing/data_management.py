import pandas as pd
import streamlit as st
from config import config

def LoadIrisDataset():
    from sklearn.datasets import load_iris
    
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df[config.TARGET_Clf1_BR2] = pd.Series(data.target)

    return df


def TrainTestSplit(df,TARGET):
    from sklearn.model_selection import train_test_split

    X_train, X_test,y_train, y_test = train_test_split(
                                        df.drop([TARGET],axis=1),
                                        df[TARGET],
                                        test_size=config.TEST_SIZE,
                                        random_state=config.RANDOM_STATE,
                                        stratify=df[TARGET]
                                        )
    st.write(" * Train Set", pd.concat([X_train,y_train], axis=1))
    st.write("* Test Set", pd.concat([X_test,y_test], axis=1))
    st.write("---")

    return X_train, X_test,y_train, y_test