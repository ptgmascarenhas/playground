"""
    Sample to test API of currency exchanges
"""

from requests import get
import json

req = get("https://api.exchangeratesapi.io/latest")
data = req.json()

print(data["rates"]["BRL"])