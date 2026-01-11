from address import Address
from mailing import Mailing

# Адрес получателя
to_address = Address(
    index="123456",
    city="Москва",
    street="Ростовская",
    house="13",
    apartment="13"
)

# Адрес отправителя
from_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Московская",
    house="12",
    apartment="12"
)

# Почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=2500,
    track="RU123456789"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")