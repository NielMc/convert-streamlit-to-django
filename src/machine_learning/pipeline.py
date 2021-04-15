from config import config
from sklearn.pipeline import Pipeline

from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

from mlxtend.classifier import StackingClassifier
from sklearn.linear_model import LogisticRegression

ClfIrisSpecies_DT = Pipeline(
    [       
        ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
        ("feat_scaling",StandardScaler()),
        ("model", DecisionTreeClassifier())
    ]
)

ClfIrisSpecies_GB = Pipeline(
    [       
        ("feat_selection",SelectFromModel(GradientBoostingClassifier(random_state=config.RANDOM_STATE))),
        ("feat_scaling",StandardScaler()),
        ("model", GradientBoostingClassifier(random_state=config.RANDOM_STATE,learning_rate=0.1))
    ]
)


ClfIrisSpecies_RF = Pipeline(
    [       
        ("feat_selection",SelectFromModel(RandomForestClassifier(random_state=config.RANDOM_STATE))),
        ("feat_scaling",StandardScaler()),
        ("model",RandomForestClassifier(
                                        random_state=config.RANDOM_STATE,
                                        n_estimators=50,criterion='gini',max_depth=12
                                        )
        )
    ]
)



ClfIrisStacking = StackingClassifier(
    classifiers=[
        ClfIrisSpecies_DT,
        ClfIrisSpecies_GB,
        ClfIrisSpecies_RF
    ],
    use_probas=True,
    meta_classifier=LogisticRegression(solver='liblinear')
)

