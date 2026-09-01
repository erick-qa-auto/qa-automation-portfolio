import requests
import json

BASE_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"



# проверка статус кода и что ответ не пустой
 
def test_apod_status_ok():
    url = BASE_URL
    response = requests.get(url)
    print("status", response.status_code)
    print("answer", response.text[:200])
    assert response.status_code == 200
    assert len(response.text) > 0


#проверка все поля на месте

def test_apod_fields_present():
    url = BASE_URL
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "explanation" in data
    assert "media_type" in data
    assert data["media_type"] in ["image", "video"]
    assert "service_version" in data
    assert "title" in data
    assert "url" in data


#проверка типы данных

def test_apod_data_types():
    url = BASE_URL
    response = requests.get(url)
    data = response.json()
    assert isinstance(data["date"], str)
    assert isinstance(data["explanation"], str)
    assert isinstance(data["media_type"], str)
    assert isinstance(data["title"], str)
    assert isinstance(data["url"], str)


# проверка url

def test_check_url():
    url = BASE_URL
    response = requests.get(url)
    data = response.json()
    media_response = requests.get(data["url"])
    assert media_response.status_code == 200
    assert data["url"].startswith("https://")
    content_type = media_response.headers["Content-Type"]
    assert content_type.startswith("video/") or content_type.startswith("image/")


#проверка bonduaries date граничное значение даты

def test_apod_date_boudaries():
    bad_dates = ["2099-01-01, 1899-01-01"]
    for date in bad_dates:
        url = f"{BASE_URL}&date={date}"
        response = requests.get(url)
        assert response.status_code != 200

def test_apod_date_before_after():
    url_main = f"{BASE_URL}&date=2026-09-01"
    response_main = requests.get(url_main)
    assert response_main.status_code == 200
    title_main = response_main.json()["title"] # запомнили title в переменную
    #день позже
    url_after = f"{BASE_URL}&date=2026-08-31"
    response_after = requests.get(url_after)
    if response_after.status_code == 200:
    # если ок то title отличается
        assert response_after.json()["title"] != title_main
    else:
        #пришла ошибка title не трогаем, просто фиксируем
        print("день позже дал ошибку, статус:", response_after.status_code)
    #день раньше
    url_before = f"{BASE_URL}&date=2026-09-02"
    response_before = requests.get(url_before)
    if response_before.status_code == 200:
        assert response_before.json()["title"] != title_main
    else:
        print("день раньше дал ошибку, статус:", response_before.status_code)