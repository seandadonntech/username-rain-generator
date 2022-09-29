import random
import pyfiglet
from colorama import Fore
result = pyfiglet.figlet_format("username-rain-generator", font = "roman" )
print(result)
print(Fore.GREEN + 'A  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, Copyright (c) 2022, lilcryptotech All rights reserved. ')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the my username Generator!")
nr_letters = int(input("How many letters would you like in your username?\n")) #0 for none
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
username_list = []

for char in range(1, nr_letters + 1):
  username_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  username_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  username_list += random.choice(numbers)

print(username_list)
random.shuffle(username_list)
print(username_list)

username = ""
for char in username_list:
  username += char

print(f"Your username is: {username}")


