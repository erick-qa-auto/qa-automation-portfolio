import requests  # Загружаем библиотеку для отправки HTTP-запросов

def test_mock_demo():  # Создаём тестовую функцию (pytest найдёт её по префиксу test_)
    url = "https://jsonplaceholder.typicode.com/users"  # Адрес API, куда будем стучаться
    new_user = {"name": "Erick"}  # Создаём словарь (карточку) с данными нового пользователя
    response = requests.post(url, json=new_user)  # Отправляем POST-запрос (создать) на сервер, получаем ответ
    print(f"POST статус: {response.status_code}")  # Выводим код ответа (201 = создано успешно)
    print(f"POST ответ: {response.json()}")  # Выводим всё, что вернул сервер (словарь с id)
    created_id = response.json()["id"]  # Достаём из ответа значение по ключу "id" (число 11)
    print(f"Создан id: {created_id}")  # Проверяем, что id действительно достался
    check_url = f"https://jsonplaceholder.typicode.com/users/{created_id}"  # Собираем URL для проверки через f-строку (подставляем id)
    check_response = requests.get(check_url)  # Отправляем GET-запрос (спросить) на этот URL
    print(f"GET статус: {check_response.status_code}")  # Выводим статус (будет 404, потому что мок не сохранил данные)
    real_user_response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(f"GET на реального пользователя статус: {real_user_response.status_code}")