import math

def square(sid):
    return sid * sid

side = float(input("Введите сторону квадрата? "))

print(square(math.ceil(side)))

