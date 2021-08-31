import requests
import json
response = requests.get("https://rickandmortyapi.com/api/character")
print(response.json())


