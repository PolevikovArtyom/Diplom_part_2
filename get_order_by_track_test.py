import sender_stand_request

# Тест проверки статуса
def test_get_order_by_track():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200