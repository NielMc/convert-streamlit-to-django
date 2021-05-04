import pandas as pd
import streamlit as st
from config import config
import joblib
_version = config.version_model # __init__.__version__

def LoadIrisDataset():
    from sklearn.datasets import load_iris
    
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df[config.ClfIrisSpecies_TARGET] = pd.Series(data.target)

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
    
    # st.write(" * Train Set", pd.concat([X_train,y_train], axis=1))
    # st.write("* Test Set", pd.concat([X_test,y_test], axis=1))
    # st.write("---")

    return X_train, X_test,y_train, y_test



def SavePipeline(*, pipeline_to_save,model_name) -> None:
    
    save_file_name = f"{model_name}_v{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    joblib.dump(pipeline_to_save, save_path)


def LoadPipeline(*, model_name):

    file_path = f"{config.TRAINED_MODEL_DIR}/{model_name}_v{_version}.pkl"
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline


def SaveTrainTestSets(model_name,target,X_train, X_test, y_train, y_test):
    
    X_train.to_csv(
    	f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.X_TRAIN_SET}_v{_version}.csv",
        index=False)

    X_test.to_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.X_TEST_SET}_v{_version}.csv",
    	index=False)

    df_y_train = pd.DataFrame(y_train,columns=[target])
    df_y_train.to_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.Y_TRAIN_SET}_v{_version}.csv",
        index=False)

    df_y_test = pd.DataFrame(y_test,columns=[target])
    df_y_test.to_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.Y_TEST_SET}_v{_version}.csv",
        index=False)
    
    

def LoadTrainTestSets(model_name):
    
    X_train = pd.read_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.X_TRAIN_SET}_v{_version}.csv"
        )
    
    y_train = pd.read_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.Y_TRAIN_SET}_v{_version}.csv"
    )

    X_test = pd.read_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.X_TEST_SET}_v{_version}.csv"
    )
    
    y_test = pd.read_csv(
        f"{config.DATASET_OUTPUT_DIR}/{model_name}_{config.Y_TEST_SET}_v{_version}.csv"
    )
    
    return X_train, X_test, y_train, y_test
