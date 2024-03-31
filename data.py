import requests
from constants import *

def get_data():
    response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS, timeout=20)
    response.raise_for_status()
    return response.json()["results"]

question_data = get_data()
