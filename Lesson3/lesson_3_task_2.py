from smartphone import Smartphone

iphoen = Smartphone("iPhone", "X", "+79274754747")
realme = Smartphone("Realme", "11", "+79274654248")
nokia = Smartphone("Nokia", "3310", "+792714648248")
poco = Smartphone("Poco", "X6", "+79274254272")
motorola = Smartphone("Motorola", "razer", "+79274624262")



catalog = []
catalog.append(iphoen)
catalog.append(realme)
catalog.append(nokia)
catalog.append(poco)
catalog.append(motorola)

for i in catalog:
    print(i.brand + " - " + i.model +". "+ i.numberPhone)
