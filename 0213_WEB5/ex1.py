import requests
import json


# Пример 1.
map_request = "https://static-maps.yandex.ru/v1?ll=37.677751,55.757718&spn=0.016457,0.00619&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
response = requests.get(map_request)
print(response)
# if response:
    # json_resp = response.json()
    # print(json_resp)



# Пример 2
api_server = "https://static-maps.yandex.ru/v1"
lon = "37.677751"
lat = "55.757718"
delta1 = "0.016457"
delta2 = "0.00619"
apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta1, delta2]),
    "apikey": apikey,
}
response = requests.get(api_server, params=params)
if response:
    print(response, type(response))

