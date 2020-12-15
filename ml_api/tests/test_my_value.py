import json
from regression_model.processing.data_management import load_dataset
from regression_model.config import config

def test_value_type(flask_test_client):
    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient='records')
    response = flask_test_client.post('/ani', json=json.loads(post_json))

    print(response.data)
