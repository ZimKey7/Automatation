from address import Address
from mailing import Mailing


Pochta = Mailing()

Pochta.setToAders("124456", "Москва", "Ольховая", "54", "235")
Pochta.setFromAders("124256", "Тула", "Гвардейская", "24", "125")
Pochta.setTrack("RED1245F")
Pochta.setCost(4499)


print(f"Отправление {Pochta.track} из {Pochta.to_address.getAddress()} в {Pochta.from_address.getAddress()}. Стоимость {Pochta.cost} рублей.")