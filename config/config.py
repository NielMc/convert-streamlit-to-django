import pathlib


# directory name
PACKAGE_ROOT = pathlib.Path().resolve()
DATASET_INPUT_DIR = PACKAGE_ROOT / "inputs/datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "outputs/trained_models"

# ML parameters
TEST_SIZE=0.2
RANDOM_STATE=0
 
#  Clf1_BR2
TARGET_Clf1_BR2 = "Species"
Clf1_BR2_name = "Clf1_BR2"
