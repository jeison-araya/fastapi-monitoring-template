import time 
import requests
import random


url = "http://localhost:8000/"
endpoint_1 = "delay/"
endpoint_2 = "error/"

def call_endpoint_1():
    response = requests.get(url + endpoint_1)
    print(response.json())


def call_endpoint_2():
    response = requests.get(url + endpoint_2)
    print(response.json())


while True:
    try: 
        time.sleep(2)
        response = requests.get(url)
        print(response.json())

        for _ in range(random.randint(0, 3)):
            call_endpoint_1()

        time.sleep(3)

        for _ in range(random.randint(0, 3)):
            call_endpoint_2()
    except:
        print("Error to connect with API")

