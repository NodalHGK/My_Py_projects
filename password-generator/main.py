import random
import list

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# password = ""
# #nr_letters = 4
# for char in range(1, nr_letters + 1):
#     password += random.choice(list.letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(list.symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(list.numbers)
    
# print(password)
    


password_list = []
#nr_letters = 4
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(list.letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(list.symbols)

for char in range(1, nr_numbers + 1):
   password_list += random.choice(list.numbers)
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char   

print(f"You password is: {password}") 
    
