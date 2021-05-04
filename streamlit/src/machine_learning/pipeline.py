from config import config
from sklearn.pipeline import Pipeline

from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier 


ClfIrisSpecies_DT = Pipeline(
    [       
        ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
        ("feat_scaling",StandardScaler()),
        ("model", DecisionTreeClassifier())
    ]
)


