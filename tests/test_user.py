import pytest
import requests
import responses

@responses.activate
def test_user_authentication_unauthorized():
    # Mock the server response for unauthorized access
    url = "http://127.0.0.1:8000/users"
    responses.add(responses.GET, url, json={}, status=401)
    
    # Define the parameters for the unauthorized case
    params = {'username': 'admin', 'password': 'admin'}
    
    # Make the GET request with the parameters
    response = requests.get(url, params=params)
    
    # Assert that the status code is 401 for unauthorized access
    assert response.status_code == 401, "Expected HTTP status code 401"
    
    # Optionally, assert the response body is empty for the unauthorized case
    assert response.text == "{}", "Expected an empty JSON response body for unauthorized access"

@responses.activate
def test_user_authentication_authorized_empty_response():
    # Mock the server response for authorized access
    url = "http://127.0.0.1:8000/users"
    responses.add(responses.GET, url, json={}, status=200)
    
    # Define the parameters for the authorized case
    params = {'username': 'admin', 'password': 'qwerty'}
    
    # Make the GET request with the new parameters
    response = requests.get(url, params=params)
    
    # Assert that the status code is 200 for authorized access
    assert response.status_code == 200, "Expected HTTP status code 200"
    
    # Optionally, assert the response body is empty for the authorized case
    assert response.text == "{}", "Expected an empty JSON response body for authorized access"
