import pathlib

import regression_model

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'train.csv'
TARGET = 'SalePraice'

# variables
FEATURES = [
    "MSSubClass",
    "MSZoning",
    "Neighborhood",
    "OverallQual",
    "OverallCond",
    "YearRemodAdd",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "1stFlrSF",
    "GrLivArea",
    "BsmtFullBath",
    "KitchenQual",
    "Fireplaces",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageCars",
    "PaveDrive",
    "LotFrontage",
    "YrSold",
]

DROP_FEATURES = "YrSold"

NUMERICAL_VARS_WITH_NA = ["LotFrontage"]

CATEGORICAL_VARS_WITH_NA = [
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",

]

TEMPORAL_VARS = "YearRemodAdd"

NUMERICAL_LOG_VARS = [ "LotFrontage", "1stFlrSF", "GrLivArea"]

CATEGORICAL_VARS = [
    "MSZoning",
    "Neighborhood",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "KitchenQual",
    "FireplaceQU",
    "GarageType",
    "GarageFinish",
    "PaveDrive",
]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in features 
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
    ]

CATEGORICAL_NA_NOT_ALLOWED = [ feature for feature in CATEGORICAL_VARS if features not in CATEGORICAL_VARS_WITH_NA]