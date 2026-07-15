from datetime import datetime
import math

name = input("What is your name?")
country = input("Where are you from?")
age = input("How old are you?")

print("Hello,", name, "from", country, "! Looks like you were born in", str(datetime.now().year - int(age)))


print("Now let's do some math.")
radius = float(input("Give me a radius for circle:"))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print("Area od circle:", str(area_of_circle))
print("Circum of circle:", str(circum_of_circle))