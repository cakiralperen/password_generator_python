import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#print(random.sample(letters, nr_letters))
#print(random.sample(numbers, nr_numbers))
#print(random.sample(symbols, nr_symbols))

random_harf = random.sample(letters, nr_letters)
random_rakam = random.sample(numbers, nr_numbers)
random_sembol = random.sample(symbols, nr_symbols)

password = random_harf + random_rakam + random_sembol
#print(password)

random.shuffle(password)
#print(password)

new_password = ''.join(password)

print(f"Your generated password is: {new_password}")