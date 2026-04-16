import pytest
from models import StudentDB

class TestStudentOperations:

    # Позитивный тест на создание студента
    def test_create_student(self, db_connection):
        """Тест добавления нового студента."""
        db = StudentDB(db_connection)
        student_name = "Иван Петров"
        student_email = "ivan.petrov@example.com"
        expected_student_count_before = len(db.get_all_students())

        new_student = db.create_student(student_name, student_email)
        expected_student_count_after = len(db.get_all_students())

        assert new_student is not None, "Студент не был создан"
        assert new_student["name"] == student_name
        assert new_student["email"] == student_email
        assert expected_student_count_after == expected_student_count_before + 1, "Количество студентов не увеличилось"

    # Позитивный тест на обновление данных студента
    def test_update_student_email(self, db_connection):
        """Тест обновления email студента."""
        db = StudentDB(db_connection)

        original_student = db.create_student("Мария Сидорова", "maria@old.com")
        new_email = "maria@new.com"

        updated_student = db.update_student_email(original_student["id"], new_email)

        assert updated_student is not None
        assert updated_student["id"] == original_student["id"]
        assert updated_student["name"] == original_student["name"]
        assert updated_student["email"] == new_email

        student_from_db = db.get_student_by_id(original_student["id"])
        assert student_from_db["email"] == new_email

    # Позитивный тест на удаление студента
    def test_delete_student(self, db_connection):
        """Тест удаления студента."""
        db = StudentDB(db_connection)

        student_to_delete = db.create_student("Петр Иванов", "petr@example.com")
        student_id = student_to_delete["id"]
        
        assert db.get_student_by_id(student_id) is not None
        
        expected_student_count_before = len(db.get_all_students())

        db.delete_student_by_id(student_id)

        expected_student_count_after = len(db.get_all_students())
        assert db.get_student_by_id(student_id) is None, "Студент все еще существует в БД"
        assert expected_student_count_after == expected_student_count_before - 1, "Количество студентов не уменьшилось"

    # Негативный тест 
    def test_create_student_duplicate_email(self, db_connection):
        """Тест на создание двух студентов с одинаковым email."""

        db = StudentDB(db_connection)
        common_email = "duplicate@example.com"
        db.create_student("Первый Студент", common_email)

        with pytest.raises(Exception): 
            db.create_student("Второй Студент", common_email)