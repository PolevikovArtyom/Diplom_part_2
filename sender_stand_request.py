import configuration
import data
import requests

#1. Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

#2. Получение трек-номера
def get_order_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]

#3. Получение заказа по треку
def get_order_by_track():
    track_with_id = str(get_order_track())
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track_with_id)

#Для ручной проверки функции
#resopnse = get_order_by_track();
#print(resopnse.status_code)
#print(resopnse.text)