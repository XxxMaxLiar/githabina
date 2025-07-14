from app import app  # Импортируем Flask-приложение
import pytest

# Фикстура для создания тестового клиента Flask
@pytest.fixture
def client():
    app.config["TESTING"] = True  # Включаем тестовый режим
    with app.test_client() as client:
        yield client

# Тест для главной страницы
def test_hello_route(client):
    response = client.get("/")  # Отправляем GET-запрос
    assert response.status_code == 200  # Проверяем код ответа
    assert b"hello world!" in response.data  # Проверяем содержимое