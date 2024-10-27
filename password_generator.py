import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to password generator")
nr_letters = int(input("How many letters would you like your password?\n "))
nr_numbers = int(input("How many numbers would you like your password?\n "))
nr_symbols = int(input("How many symbols would you like your password?\n "))

#password = ""
#for i in range(0, nr_letters):

#random.choice(letters)
    #password =password+random.choice(letters)

#for i in range(0,nr_numbers):
    #random.choice(numbers)

#   password =password+random.choice(numbers)

#for i in range(0,nr_symbols):
    #random.choice(symbols)
    #password =password+random.choice(symbols)
#print(password)
password_list=[]
for i in range(0,nr_letters):
    random.choice(letters)
    password_list.append(random.choice(letters))
for i in range(0,nr_numbers):
    random.choice(numbers)
    password_list.append(random.choice(numbers))
for i in range (0,nr_symbols):
    random.choice(symbols)
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password=password+i
print(password)