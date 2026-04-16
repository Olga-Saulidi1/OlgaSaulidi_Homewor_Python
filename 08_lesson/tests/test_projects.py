import pytest
from pages.project_api import ProjectAPI


class TestProjectsAPI:
    """Набор автотестов для API проектов Yougile"""
    
    @pytest.fixture(autouse=True)
    def setup(self, base_url, auth_headers, board_id):
        self.api = ProjectAPI(base_url, auth_headers, default_board_id=board_id)
        self.created_projects = []  # Список созданных проектов для очистки
    
    def _cleanup_projects(self):
        """Очистка созданных проектов после тестов"""
        for project_id in self.created_projects:
            try:
                self.api.delete_project(project_id)
                print(f"Очистка: удален проект {project_id}")
            except Exception as e:
                print(f"Не удалось удалить проект {project_id}: {e}")
    
    @pytest.fixture(autouse=True)
    def cleanup(self):
        """Автоматическая очистка после каждого теста"""
        yield
        self._cleanup_projects()

    # ============ POST /api-v2/projects ============
    
    def test_create_project_positive(self, unique_project_name):
        """Позитивный тест: создание проекта с минимальными данными"""
        response = self.api.create_project(title=unique_project_name)
        
        assert response.status_code == 201, (
            f"Ожидался 201, получен {response.status_code}\n"
            f"Тело ответа: {response.text}"
        )
        
        response_json = response.json()
        assert "id" in response_json, "Ответ не содержит id созданного проекта"
        
        project_id = response_json["id"]
        self.created_projects.append(project_id)  # Запоминаем для очистки
        
        # Проверяем, что в ответе есть id (Yougile не возвращает title в ответе)
        assert project_id is not None, "ID проекта не должен быть None"
        assert len(project_id) > 0, "ID проекта не должен быть пустым"

    def test_create_project_without_title_negative(self):
        """Негативный тест: создание проекта без имени"""
        response = self.api.create_project(title="")
        
        # Yougile возвращает 400 при пустом title
        assert response.status_code == 400, (
            f"Ожидалась ошибка 400, получен {response.status_code}"
        )
        
        response_json = response.json()
        # Проверяем, что есть сообщение об ошибке
        assert "message" in response_json or "error" in response_json

    # ============ GET /api-v2/projects/{id} ============
    
    def test_get_project_positive(self, unique_project_name):
        """Позитивный тест: получение существующего проекта по ID"""
        # Создаем проект
        create_response = self.api.create_project(title=unique_project_name)
        assert create_response.status_code == 201, (
            f"Не удалось создать проект: {create_response.text}"
        )
        
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)  # Запоминаем для очистки
        
        # Получаем проект по ID
        get_response = self.api.get_project(project_id)
        
        assert get_response.status_code == 200, (
            f"Ожидался 200, получен {get_response.status_code}\n"
            f"Тело ответа: {get_response.text}"
        )
        
        project_data = get_response.json()
        assert project_data["id"] == project_id, "ID проекта не совпадает"
        assert project_data["title"] == unique_project_name, "Название проекта не совпадает"

    def test_get_project_nonexistent_id_negative(self):
        """Негативный тест: получение проекта по несуществующему ID"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = self.api.get_project(fake_id)
        
        # Yougile возвращает 404 для несуществующего проекта
        assert response.status_code == 404, (
            f"Ожидалась ошибка 404, получен {response.status_code}"
        )

    # ============ PUT /api-v2/projects/{id} ============
    
    def test_update_project_title_positive(self, unique_project_name):
        """Позитивный тест: изменение имени проекта"""
        # Создаем проект
        create_response = self.api.create_project(title=unique_project_name)
        assert create_response.status_code == 201, (
            f"Не удалось создать проект: {create_response.text}"
        )
        
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)  # Запоминаем для очистки
        
        # Обновляем название
        new_title = f"{unique_project_name}_updated"
        update_response = self.api.update_project(project_id, title=new_title)
        
        assert update_response.status_code == 200, (
            f"Ожидался 200, получен {update_response.status_code}\n"
            f"Тело ответа: {update_response.text}"
        )
        
        # Важно: PUT запрос может не возвращать обновленные данные
        # Поэтому проверяем через GET запрос, что название действительно изменилось
        get_response = self.api.get_project(project_id)
        assert get_response.status_code == 200, "Не удалось получить обновленный проект"
        
        project_data = get_response.json()
        assert project_data["title"] == new_title, (
            f"Название не обновилось. Ожидалось: {new_title}, "
            f"Получено: {project_data.get('title')}"
        )

    def test_update_project_nonexistent_id_negative(self):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = self.api.update_project(fake_id, title="New Name")
        
        # Yougile возвращает 404 для несуществующего проекта
        assert response.status_code == 404, (
            f"Ожидалась ошибка 404, получен {response.status_code}"
        )