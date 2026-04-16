import requests


class ProjectAPI:
    """Класс для работы с API проектов Yougile (PageObject)"""

    def __init__(self, base_url, auth_headers, default_board_id=None):
        self.base_url = base_url
        self.auth_headers = auth_headers
        self.default_board_id = default_board_id

    def create_project(self, title):
        """
        POST /api-v2/projects - создание проекта
        
        Согласно документации Yougile:
        - title: название проекта (обязательное поле)
        """
        url = f"{self.base_url}/api-v2/projects"
        
        # Yougile принимает только title при создании
        payload = {
            "title": title
        }

        response = requests.post(url, json=payload, headers=self.auth_headers)
        return response

    def get_project(self, project_id):
        """
        GET /api-v2/projects/{id} - получение проекта по ID
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.auth_headers)
        return response

    def update_project(self, project_id, title=None):
        """
        PUT /api-v2/projects/{id} - обновление проекта
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        
        payload = {}
        if title is not None:
            payload["title"] = title

        response = requests.put(url, json=payload, headers=self.auth_headers)
        return response

    def get_boards(self):
        """
        GET /api-v2/boards - получение списка досок
        """
        url = f"{self.base_url}/api-v2/boards"
        response = requests.get(url, headers=self.auth_headers)
        return response

    def get_all_projects(self, limit=100, offset=0):
        """
        GET /api-v2/projects - получение списка проектов
        """
        url = f"{self.base_url}/api-v2/projects"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, headers=self.auth_headers, params=params)
        return response
    
    def delete_project(self, project_id):
        """
        DELETE /api-v2/projects/{id} - удаление проекта
        (для очистки тестовых данных)
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.delete(url, headers=self.auth_headers)
        return response