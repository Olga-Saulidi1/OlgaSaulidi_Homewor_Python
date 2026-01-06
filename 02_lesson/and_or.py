user_login = "adam"
user_pass = "zaq123"

login = input ("Login: ")
password = input ("Password: ")

if (login == user_login) and (password == user_pass):
    print ("Secret is open")
else:
    print ("pu-pu-pu")

crit1 = "red"
crit = "lock"

color = input ("Color: ")
feature = input ("Feature: ")

if (color ==crit1) or (feature==crit):
    print("Покупаем")
else:
    print("BEEEEEE")