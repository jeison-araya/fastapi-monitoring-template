import time 
import requests

url = "http://localhost:8000/"
endpoint_1 = "delay/"
endpoint_2 = "error/"

while True:
    try: 
        time.sleep(1)
        response = requests.get(url)
        print(response.json())
    except:
        print("Error to connect with API")


def call_endpoint_1():
    response = requests.get(url + endpoint_1)
    print(response.json())


def call_endpoint_2():
    response = requests.get(url + endpoint_2)
    print(response.json())