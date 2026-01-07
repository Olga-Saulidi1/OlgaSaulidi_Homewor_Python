from smartphone import Smartphone
catalog = [
    Smartphone ("Iphone", "17", "+7911 111 11 11"),
    Smartphone ("Samsung", "A10", "+7922 222 22 22"),
    Smartphone ("Xiomi", "S13", "+7933 333 33 33"),
    Smartphone ("Redmi", "Note 9 pro", "+7944 444 44 44"),
    Smartphone ("Techno", "S14", "+7955 555 55 55")
]
for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.phone_number}")
