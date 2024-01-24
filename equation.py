# Program to solve quadratic equations
import math

a = float(input("a: "))
while a == 0:
    a = float(input("a: "))

b = float(input("b: "))
c = float(input("c: "))

try:
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
    print(f"x1 = {x1}, x2 = {x2}")
except ValueError:
    print("No Real roots :(")

