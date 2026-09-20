import requests
import logging

logging.basicConfig(level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

def test_logging_demo():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    logging.info(f"status: {response.status_code}")
    logging.warning("предупреждения")
    logging.error("ошибка но тест продолжился")
    assert response.status_code == 200

if __name__ == "__main__":
    test_logging_demo()