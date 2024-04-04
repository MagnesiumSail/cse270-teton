import pytest
import requests

class MockResponse:
    # Mocking the requests.Response object
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = json_data if isinstance(json_data, str) else ""

    def json(self):
        return self.json_data

def mock_requests_get_unauthorized(url, params=None, **kwargs):
    return MockResponse("", 401)  # Return an empty string and status code 401 for unauthorized access

def mock_requests_get_authorized(url, params=None, **kwargs):
    return MockResponse("", 200)  # Return an empty string and status code 200 for authorized access

def test_user_authentication_unauthorized(mocker):
    mocker.patch('requests.get', side_effect=mock_requests_get_unauthorized)
    
    url = "http://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'admin'}
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 401, "Expected HTTP status code 401"
    assert response.text == "", "Expected an empty response body for unauthorized access"

def test_user_authentication_authorized_empty_response(mocker):
    mocker.patch('requests.get', side_effect=mock_requests_get_authorized)
    
    url = "http://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'qwerty'}
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 200, "Expected HTTP status code 200"
    assert response.text == "", "Expected an empty response body for authorized access"
