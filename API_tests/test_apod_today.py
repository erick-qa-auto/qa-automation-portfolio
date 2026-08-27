import requests

def test_nasa_apod_future_date():
    # 1. Делаем запрос с датой из будущего (твоя идея!)
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2099-01-01")
    
    # 2. Проверяем, что это НЕ успешный ответ (не 200)
    assert response.status_code != 200
    
    # 3. Мы НЕ используем response.json(), потому что при ошибке сервер 
    # может прислать не JSON, а простой текст или HTML, и .json() сломает тест.
    # Вместо этого мы просто посмотрим, что сервер вообще что-то ответил:
    assert len(response.text) > 0
    
    