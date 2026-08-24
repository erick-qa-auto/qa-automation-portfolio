# test 1 Successful server response
import requests
def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    
