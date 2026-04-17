from sqlalchemy import text


class StudentDB:

    def __init__(self, connection):
        self.conn = connection

    def create_student(self, name, email):
        # Добавление нового студента
        query = text("""
            INSERT INTO students (name, email)
            VALUES (:name, :email)
            RETURNING id, name, email
        """)
        result = self.conn.execute(query, {"name": name, "email": email})
        return result.mappings().first()

    def get_student_by_id(self, student_id):
        # Получение студента по ID
        query = text("SELECT id, name, email FROM students WHERE id = :id")
        result = self.conn.execute(query, {"id": student_id})
        return result.mappings().first()

    def update_student_email(self, student_id, new_email):
        # Обновление email студента
        query = text("""
            UPDATE students SET email = :email
            WHERE id = :id
            RETURNING id, name, email
        """)
        result = self.conn.execute(
            query, {"id": student_id, "email": new_email})
        return result.mappings().first()

    def delete_student_by_id(self, student_id):
        # Удаление студента по ID
        query = text("DELETE FROM students WHERE id = :id")
        self.conn.execute(query, {"id": student_id})

    def get_all_students(self):
        # Получение всех студентов
        query = text("SELECT id, name, email FROM students")
        result = self.conn.execute(query)
        return result.mappings().all()
