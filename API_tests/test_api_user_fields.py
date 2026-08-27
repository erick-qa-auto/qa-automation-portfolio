import requests

#посмотрели статус и посмотрели ответ
def test_user_full_check():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.status_code)
    print(response.text)
    assert len(response.text) > 0

#test 1: проверим что поле email - почта а не имя
def test_user_email_or_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    user_data = response.json()
    assert response.status_code == 200
    assert "@" in user_data["email"]
    assert "@" not in user_data["name"]

#test 2: проверим оригинальный ли username пользователя
def test_user1_username():
     response = requests.get("https://jsonplaceholder.typicode.com/users")
     users = response.json()
     print(response.json)
     usernames = []
     for user in users:
         usernames.append(user["username"])
     assert usernames.count("Bret") == 1

#test 3: провверка типы данных
def test_user_data_types():
     response = requests.get("https://jsonplaceholder.typicode.com/users/1")
     user_data = response.json()
     assert isinstance(user_data["id"], int)
     assert isinstance(user_data["name"], str)


#test 4: место жительство (вложенные поля)
def test_user_city():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    user_data = response.json()
    assert response.status_code == 200
    assert user_data["address"]["city"] == "Gwenborough"



# test 5: проверка наличие полей
def test_presence_of_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    user_data = response.json()
    assert "name" in user_data
    assert "id" in user_data
    assert "username" in user_data
    assert "email" in user_data




#test 6: negative tests unreal id
def test_negative_invalid_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert response.status_code != 200
    
    