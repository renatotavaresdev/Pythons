import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]

print('Bem vindo ao gerador de senhas!')
nr_letters = int(input('Quantas letras você quer na sua senha? '))
nr_symbols = int(input('Quantos Simbolos você quer na sua senha? '))
nr_number = int(input('Quantos números você quer na sua senha? '))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
    
for char in range(1, nr_number + 1):
    password_list += random.choice(numbers)
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    
print(f'Sua Senha é {password}')

import time
time.sleep(60)