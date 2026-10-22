import requests
import logging
logger = logging.getLogger(__name__)

def test_nasa_apod_data():
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": "YOUR_API_KEY_HERE"}
    response = requests.get(url, params=params)
    logger.info(f"Status code: {response.status_code}")
    logger.info(f"JSON response: {response.text}")
    data = response.json()
    logger.info(f"type of data: {type(data)}")
    logger.info(f"date: {data['date']}")
    logger.info(f"title: {data['title']}")