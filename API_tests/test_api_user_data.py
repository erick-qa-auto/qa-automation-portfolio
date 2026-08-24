import requests

def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    user_data = response.json()
    print(user_data)
    assert user_data["id"] == 1
    assert user_data["name"] == "Leanne Graham"
    assert user_data["email"] == "Sincere@april.biz"