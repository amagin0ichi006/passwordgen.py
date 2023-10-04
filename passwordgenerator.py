import random
print("welcome to pypassword generator")
letters = ["A", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "O", "P","q", "R", "s", "t" "r","u", "v", "w", "x", "y", "z","Z", "B", "S"]
symbols = ["@", "!", "#", "$", "%", "^", "&", "*", "~",]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
num_letters = int(input("how many letters do you want"))
num_symbols = int(input("how many symbols do you want"))
num_numbers =int(input("how many numbers would you like"))
password = ""
for l in range(0, num_letters):
    random_char = random.choice(letters)
    password += random_char
for s in range(0, num_symbols):
    random_symb = random.choice(symbols)
    password += random_symb
for num in range(0, num_numbers):
    random_num = random.choice(numbers)
    password += random_num
   
print(f"here is your password bitch {password}")


