import pandas as pd
from config import config
import joblib


def LoadIrisDataset():
    return pd.read_csv("inputs/datasets/Iris.csv")


def TrainTestSplit(df,TARGET):
    from sklearn.model_selection import train_test_split

    X_train, X_test,y_train, y_test = train_test_split(
                                        df.drop([TARGET],axis=1),
                                        df[TARGET],
                                        test_size=config.TEST_SIZE,
                                        random_state=config.RANDOM_STATE,
                                        stratify=df[TARGET]
                                        )

    return X_train, X_test,y_train, y_test






def LoadPipeline(*, model_name, path):

    file_path = f"{path}/{model_name}.pkl"
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline


    

def LoadTrainTestSets(model_name,path):
    
    X_train = pd.read_csv(f"{path}/{model_name}_Xtrain.csv")
    
    y_train = pd.read_csv(f"{path}/{model_name}_ytrain.csv")
    
    X_test = pd.read_csv(f"{path}/{model_name}_Xtest.csv")
    
    y_test = pd.read_csv(f"{path}/{model_name}_ytest.csv")
    
    return X_train, X_test, y_train, y_test
