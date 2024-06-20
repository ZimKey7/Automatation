def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

yars = input("Укажите год? ")

sign = is_year_leap(int(yars))

print("год "+ yars + ": " + str(sign))