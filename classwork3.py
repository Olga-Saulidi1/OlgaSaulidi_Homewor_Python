from user import User
from card import Card

papa = User("papa")

papa.seyName ()
papa.setAge (33)
papa.seyAge ()

card = Card ("1234 1234 1234 1234", "01/26", "papa")

papa.addCard (card)
papa.getCard ().pay(5000)

Olga = User ("Olga")
Olga.seyName ()