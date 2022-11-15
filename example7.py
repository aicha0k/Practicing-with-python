import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password =[]
print("welcome to the password generator\n")
nr_letters = int(input("how many letters do you want in your password?\n"))
nr_numbers = int(input("how many numbers do you want in your password?\n"))
nr_symbols = int(input("how many symbols do you want in your password?\n"))
for i in range(1, nr_letters+1):
    password.append(random.choice(letters))
for i in range(1, nr_numbers+1):
    password.append(random.choice(numbers))
for i in range(1, nr_symbols+1):
    password.append(random.choice(symbols))
random.shuffle(password)
your_passowrd = "".join(password)
print("your password is:", your_passowrd)

    