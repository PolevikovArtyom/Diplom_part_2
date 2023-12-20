import configuration
import data
import requests

#1. Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

#2. Получение заказа по параметру
def get_order_by_parameter(track_number):
    track_with_id = str(track_number)
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track_with_id)