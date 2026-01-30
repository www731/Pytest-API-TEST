import requests
import json


class TestPytestMultiEnvDemo:

    def test_get_demo_multi_env(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        get_api = env_config["getAPI"]
        get_api_response_data = env_response_data["getAPI"]
        # send request
        response = requests.get(host+get_api)
        # assert
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo_multi_env(self, env_config, env_request_data, env_response_data):
        host = env_config["host"]
        post_api = env_config["postAPI"]
        post_api_request_data = env_request_data["postAPI"]
        post_api_response_data = env_response_data["postAPI"]

        response = requests.post(host + post_api, json=post_api_request_data)
        resp_json = response.json()

        assert response.status_code == 201
        assert resp_json["title"] == post_api_response_data["title"]
        assert resp_json["body"] == post_api_response_data["body"]
        assert int(resp_json["userId"]) == post_api_response_data["userId"]
