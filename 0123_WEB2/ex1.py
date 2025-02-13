import requests
import json

geocod_req = "https://geocode-maps.yandex.ru/1.x/?apikey=8013b162-6b42-4997-9691-77b7074026e0&geocode=Якутск&format=json"
response = requests.get(geocod_req)


if response:
    print(response, type(response))
    json_resp = response.json()
    print(json_resp)
    with open('ex1.json', 'w', encoding='utf8') as json_file:
        json.dump(json_resp, json_file, ensure_ascii=False)
    toponym = json_resp["response"]["GeoObjectCollection"]["featureMember"][4]["GeoObject"]["Point"]["pos"]
    print(toponym)
else:
    print('Ошибка выполнения запроса:')
    print(geocod_req)
    print("HTTH статус:", response.status_code, response.reason)
