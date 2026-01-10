import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()


class TestCapitalize:
       
    # ---------- ПОЗИТИВНЫЕ СЦЕНАРИИ ----------
    @pytest.mark.positive
    def test_capitalize_non_empty_string(self, utils):
        assert utils.capitalize("skypro") == "Skypro"
        
    @pytest.mark.positive
    def test_capitalize_string_with_spaces(self, utils):
        assert utils.capitalize("привет, мир") == "Привет, мир"

  # ---------- НЕГАТИВНЫЕ СЦЕНАРИИ ----------   
    @pytest.mark.negative
    def test_capitalize_empty_string(self, utils):
        assert utils.capitalize("") == ""


class TestTrim:

    # ---------- ПОЗИТИВНЫЕ СЦЕНАРИИ ----------
    @pytest.mark.positive
    def test_trim_non_empty_string(self, utils):
        assert utils.trim("   skypro") == "skypro"

    # ---------- НЕГАТИВНЫЕ СЦЕНАРИИ ----------
    @pytest.mark.negative
    def test_trim_only_spaces(self, utils):
        assert utils.trim("   ") == ""      #строка только из пробелов


class TestContains:

   # ---------- ПОЗИТИВНЫЙ СЦЕНАРИИ ----------
    @pytest.mark.positive
    def test_contains_numbers_as_string(self, utils):
        assert utils.contains("1983", "3") == True

   # ---------- НЕГАТИВНЫЙ СЦЕНАРИИ ---------- 
    @pytest.mark.negtive
    def test_contains_non_empty_string(self, utils):
        assert utils.contains("Skypro", "T") == False


class TestDeleteSymbol:
   # ---------- ПОЗИТИВНЫЙ СЦЕНАРИИ ----------
   @pytest.mark.positive
   def test_delete_symbol_non_empty_string(self, utils):
        assert utils.delete_symbol("10.01.2026", ".") == "10012026"

   # ---------- НЕГАТИВНЫЙ СЦЕНАРИИ ---------- 
   @pytest.mark.negative
   def test_delete_symbol_not_found(self, utils):
       assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
     