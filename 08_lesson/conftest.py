import pytest
import requests
# Вставь логин и пароль из блока сдачи ДЗ в ЛК
YOUGILE_LOGIN = "..." 
YOUGILE_PASSWORD = "..."
YOUGILE_COMPANY_ID = "0410088c-8bd7-46a6-9d6f-6800117e0a96"
YOUGILE_BOARD_ID = "k3amueh58sy0"

@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"

@pytest.fixture(scope="session")
def auth_headers(base_url):
    # 1. Формируем URL для получения ключа
    auth_url = f"{base_url}/api-v2/auth/keys"
    
    # 2. Создаем payload с обязательными полями
    payload = {
        "login": YOUGILE_LOGIN,
        "password": YOUGILE_PASSWORD,
        "companyId": YOUGILE_COMPANY_ID
    }
    
    # 3. Отправляем POST-запрос на создание ключа
    response = requests.post(auth_url, json=payload)
    
    # 4. Проверяем, что ключ успешно создался (статус 201 Created)
    assert response.status_code == 201, (
        f"Ошибка авторизации: статус {response.status_code}\n"
        f"Тело ответа: {response.text}"
    )
    
    # 5. Извлекаем ключ из ответа 
    response_json = response.json()
    assert "key" in response_json, "Ответ не содержит поле 'key'"
    auth_key = response_json["key"]
    
    # 6. Возвращаем заголовки для всех последующих запросов
    # Ключ передается в формате Bearer Token
    return {
        "Authorization": f"Bearer {auth_key}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="session")
def board_id():
    return YOUGILE_BOARD_ID


@pytest.fixture(scope="session")
def api_client(base_url, auth_headers, board_id):
    from pages.project_api import ProjectAPI
    return ProjectAPI(base_url, auth_headers, default_board_id=board_id)


@pytest.fixture
def unique_project_name():
    import time
    return f"AutoTest_{int(time.time())}"