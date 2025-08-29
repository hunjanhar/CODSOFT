import random
import string

class password_generator:
    def __init__(self):
        print(r"""
 ____                                     _    
|  _ \ __ _ ___ _____      _____  _ __ __| |   
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |   
|_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
              
""")
        while True:
            print("1. Generate new Password 🔐\n2. Exit🚪")
            try:
                user_input = int(input("Enter the option :- "))
                if user_input == 1:
                    self.generate_password()
                elif user_input == 2:
                    break;
                else:
                    print("Invalid option ❎")
            except ValueError:
                print("Invalid Input 🔢")
    

    def generate_password(self):
        try:
            num = int(input("Enter the length of Password 🔒 :- "))
            if num <= 0:
                print("Enter the length of password greator than zero !!!")
            else:
                letters = input("Included Letters 🅰 ? (yes,no) :- ").lower() == 'yes'
                digits = input("Included Digits 🔟 ? (yes,no) :- ").lower() == 'yes'
                symbols = input("Included Symbols ⁉️ ? (yes,no):- ").lower() == 'yes'
                password = self.gen_pass(num,letters,digits,symbols)
                if password == False:
                    print("Choose some letters 🅰, digits 🔟 or symbols ⁉️ to generate password !!!")
                else:
                    print(f"\nThe password is 🔐 :- \033[92m{password}\033[0m\n")
        except ValueError:
            print("Invalid Input !!!")

    def gen_pass(self,length,letters=True,digits=True,symbols=True):
        lib = ''
        if letters:
            lib += string.ascii_letters
        if symbols:
            lib += string.punctuation
        if digits:
            lib += string.digits
        if not lib:
            return False
        else:
            password = ''.join(random.choice(lib) for _ in range(length))
            return password

obj = password_generator()

    
        