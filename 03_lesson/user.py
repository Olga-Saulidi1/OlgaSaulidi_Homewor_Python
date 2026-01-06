class User:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name (self):
        return self.first_name
    
    def get_last_name (self):
        return self.last_name
    
    def get_product_info (self):
        return f"имя: {self.first_name}, фамилия: {self.last_name}"    