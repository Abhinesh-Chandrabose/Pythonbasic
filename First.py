# Simple greet + birth year calculator
import datetime

name = input("What's your name? ")
age = int(input("How old are you? "))
birth_year = datetime.date.today().year - age

print(f"Hello, {name}! You were born in {birth_year}.")
print("Welcome to the program!")
print("This is a simple greeting and birth year calculator.")
