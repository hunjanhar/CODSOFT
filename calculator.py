class calculator:
    def __init__(self):
        print(r'''
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|                                                                                                           
''')
        self.result = self.user_start()
        if self.result or self.result == 0:
            print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
            while True:
                try:
                    print("Press the Option \n1. Addition ➕\n2. Substarction ➖\n3. Multiplication ✖️\n4. Division ➗\n5. Clean 🧼\n6. Exit 🚪")
                    userinput = int(input("Enter the Option :- "))
                    if userinput == 1:
                        self.result = self.check_option("+") 
                        print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
                    elif userinput == 2:
                        self.result = self.check_option("-")
                        print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
                    elif userinput == 3:
                        self.result = self.check_option("*")
                        print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
                    elif userinput == 4:
                        self.result = self.check_option("/")
                        print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
                    elif userinput == 5:
                        self.result = self.user_start()
                        print(f"\nThe result 🟰  \033[92m{self.result}\033[0m\n")
                    elif userinput == 6:
                        break
                    else:
                        print("Invalid Command  ❎")
                except Exception:
                    print(Exception)

    def check_option(self,operator):
        try:
            num = int(input("Enter the number 🔢:- "))
            result = self.operation_perform(self.result,num,operator)
            if result != None:
                return result
        except ValueError:
            print("Invalid Input 🔢")
            return self.result

    def user_start(self):
        while True:
            try:
                num1 = int(input("Enter the Fisrt Number 1️⃣ :- "))
                num2 = int(input("Enter the Second Number 2️⃣ :- "))
                operator = input("Enter the operator which operation you perform  ➕, ➖, ➗ or ✖️ :- ")
                res = self.operation_perform(num1,num2,operator)
                if res != False or res == 0:
                    return res
            except ValueError:
                print("Invalid Input 🔢")
    
    def operation_perform(self,num1,num2,operator):
        try:
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                return num1 / num2
            else:
                print("The operator is not Exist ❎!!!")
                return False
        except Exception:
            print(Exception)

obj = calculator()


