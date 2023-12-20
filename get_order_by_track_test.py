# Артём Полевиков, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# Используем функцию создания заказа, получаем из неё трек и подставляем в запрос получения заказа по треку
def test_get_order():
    order = sender_stand_request.post_new_order(data.order_body)
    track_number = order.json()["track"]
    response = sender_stand_request.get_order_by_parameter(track_number)
    assert response.status_code == 200
