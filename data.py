import requests
from constants import *

response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS, timeout=20)
response.raise_for_status()

question_data = response.json()["results"]
