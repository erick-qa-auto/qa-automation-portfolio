import requests
# без ключа
def test_keys_nasa():
    url = "https://api.nasa.gov/planetary/apod"
    response_missing = requests.get(url)
    print(f"MISSING status: {response_missing.status_code}")
    error_code = response_missing.json()["error"]["code"]
    print(f"missing error status code: {error_code}")
    assert response_missing.status_code == 403
    assert error_code == "API_KEY_MISSING"

# неверный ключ
def test_invalid_key():
    url = "https://api.nasa.gov/planetary/apod"
    response_invalid = requests.get(url, params={"api_key": "1234567"})
    print(f"invalid status code: {response_invalid.status_code}")
    error_code = response_invalid.json()["error"]["code"]
    print(f"invalid key error code:{error_code}")
    assert response_invalid.status_code == 403
    assert error_code == "API_KEY_INVALID"

# валидный ключ
def test_real_key():
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params={"api_key":"maCce442mbqJgS0ECBE2IPemgpbJsAaE6hesovyq"})
    print(f"status code: {response.status_code}")
    title = response.json()["title"]
    print(f"response title: {title}")
    assert response.status_code == 200
    assert title != ""