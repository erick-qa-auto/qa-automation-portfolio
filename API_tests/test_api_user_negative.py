import requests

def test_get_nonexistent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert response.status_code == 404