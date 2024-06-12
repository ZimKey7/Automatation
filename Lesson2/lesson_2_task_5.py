def month_to_season(num):
    if num < 1 and num > 12:
        print("Нет такого месяца!")
    elif num > 2 and num < 6:
        print("Весна")
    elif num > 5 and num < 9:
        print("Лето")
    elif num > 8 and num < 12:
        print("Осень")
    else:
        print("Зима")

month_to_season(int(input("Введите порядковый номер меяца? ")))