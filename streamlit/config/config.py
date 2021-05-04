import pathlib

# directory name
PACKAGE_ROOT = pathlib.Path().resolve()
DATASET_OUTPUT_DIR = PACKAGE_ROOT / "outputs/datasets"
DATASET_INPUT_DIR = PACKAGE_ROOT / "inputs/datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "outputs/trained_models"

# Saved Datasets - filenames
X_TRAIN_SET = "X_TrainSet"
Y_TRAIN_SET = "Y_TrainSet"
X_TEST_SET = "X_TestSet"
Y_TEST_SET = "Y_TestSet"


# ML parameters
TEST_SIZE=0.2
RANDOM_STATE=0
 
#  ClfIrisSpecies
ClfIrisSpecies_TARGET = "Species"
ClfIrisSpecies_NAME = "ClfIrisSpecies"
ClfIrisSpecies_MAP = {
        0:"0 - Setosa",
        1:"1 - Versicolour",
        2:"2 - Virginica"
    }

# version Model
version_model = "DT"