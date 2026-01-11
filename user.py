class User:
    age=0
    def __init__(self, name):
        print("я создался")
        self.username = name
        
    def seyName(self):
        print("Меня зовут ", self.username)

    def seyAge (self):
        print(self.age)

    def setAge (self, newAge):
        self.age=newAge    

    def addCard (self, card):
        self.card = card 

    def getCard (self):
        return self.card    