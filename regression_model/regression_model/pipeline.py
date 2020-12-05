from sklearn.pipeline import Pipeline 

import preprocessors as pp

CATEGORICAL_VARS = ['MSZoning',
                     'Neighborhood',
                     'RoofStyle',
                     'MasVnType',
                     'BsmtQual',
                     'BsmtExposure',
                     'HeatingQXC',
                     'CentralAir',
                     'KitchenQual',
                     'FireplaceQu',
                     'GarageType',
                     'GarageFinish',
                     'PavedDrive']

PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
        ('categorical_imputer',
        pp.CategoricalImputer(variables=CATEGORICAL_VARS)),
    ]
)