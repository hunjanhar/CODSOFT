import random
import getpass

class stone_paper_scissor:
    def __init__(self):
        print("""
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
""")
        self.score1 = 0
        self.score2 = 0
        while True:
            try:
                userinput = input("Choose The Play With :\n* Computer(c)💻\n* Another Player(p)👱🏻‍♀️\n* Exit(e)🚪\n")
                if userinput == "c":
                    self.comp()
                elif userinput == "p":
                    self.player() 
                elif userinput == 'e':
                    break
                else:
                    print("Invalid option ❎!!!")
            except ValueError:
                print("Enter the Correct Value 🔢!!!")

    def comp(self):
        print("\nPLAY WITH COMPUTER💻")
        def comp_play():
            try:
                inputuser = int(input("\nChoose\n* Rock(1)🪨\n* Paper(2)📄\n* Sissor(3)✂️\n"))
                if inputuser == 1 or inputuser == 2 or inputuser == 3:
                    comp = self.comp_random()
                    print("\nYou Enter 🧑 " + self.check_user_command(inputuser))
                    print("Computer Enter 💻 " + comp)       
                    self.check(self.check_user_command(inputuser),comp,'c')
                    self.score_display('c')
                else:
                    print("Invalid Input ❎\n")
            except ValueError:
                print("Enter the correct Value 🔢\n")
        comp_play()
        while True:
            print("* PLAY AGAIN(1)▶️\n* Exi(2)🚪")
            try:
                userinput = int(input("Enter the option :- "))
                if userinput == 1:
                    comp_play()
                elif userinput == 2:
                    print("THANKU FOR PLAYING ✌🏻")
                    break
                else:
                    print("Invalid Command ❎\n")
            except ValueError:
                print("Invalid Input 🔢\n")
    
    def player(self):
        print("PLAY WITH PLAYER 👱🏻‍♀️")
        print("* Note - input hides for playing 🫣!!!")
        def start_play():
            try:
                inputuser = int(getpass.getpass("player 1 Choose\n* Rock(1)🪨\n* Paper(2)📄\n* Scissor(3)✂️\n"))
                inputuser2 = int(getpass.getpass("player 2 Choose\n* Rock(1)🪨\n* Paper(2)📄\n* Scissor(3)✂️\n"))
                if (inputuser == 1 or inputuser == 2 or inputuser == 3) and (inputuser2 == 1 or inputuser2 == 2 or inputuser2 == 3):
                    print("First Player Entered 🧑 " + self.check_user_command(inputuser))
                    print("Second  Player Entered 👩 " + self.check_user_command(inputuser2))
                    self.check(self.check_user_command(inputuser),self.check_user_command(inputuser2))
                    self.score_display()
                else:
                    print("Invalid Command ❎")
            except ValueError:
                print("Invalid Input 🔢")
        start_play()
        while True:
            print("* PLAY AGAIN(1)▶️\n* Exi(2)🚪")
            try:
                userinput = int(input("Enter the option :- "))
                if userinput == 1:
                    start_play()
                elif userinput == 2:
                    print("THANKU FOR PLAYING ✌🏻")
                    break
                else:
                    print("Invalid Command ❎\n")
            except ValueError:
                print("Invalid Input 🔢\n")

    def check_user_command(self,userinput):
        if userinput == 1:
            return "Rock"
        elif userinput == 2:
            return "Paper"
        elif userinput == 3:
            return "Scissor"
    
    def score_display(self,mode='p'):
        if mode == 'c':
            print(f"\nThe user score is {self.score1} 🧑")
            print(f"The computer score is {self.score2} 💻\n")
        else:
            print(f"\nThe first player score is {self.score1} 🧑")
            print(f"The second player score is {self.score2} 👩\n")
        
    def comp_random(self):
        randomnumber = random.randint(1,3)
        if randomnumber == 1:
            return 'Rock'
        elif randomnumber == 2:
            return 'Paper'
        elif randomnumber == 3:
            return 'Scissor'
    
    def check(self,inputuser1,inputuser2,mode='p'):
        if(inputuser1 == inputuser2):
            print("\nMatch Is Tie !")
        elif((inputuser1 == 'Rock' and inputuser2 == 'Paper') or (inputuser1 == 'Paper' and inputuser2 == 'Scissor') or (inputuser1 == 'Scissor' and inputuser2 == 'Rock')):
            if mode == 'c':
                print("\nComputer is Win 🏆")
            else:
                print("\nSecond Player is Win 🏆")
            self.score2 = self.score2 + 1
        elif((inputuser1 == 'Paper' and inputuser2 == 'Rock') or (inputuser1 == 'Scissor' and inputuser2 == 'Paper') or (inputuser1 == 'Rock' and inputuser2 == 'Scissor')):
            if mode == 'c':
                print("\nThe user is Win 🏆")
            else:
                print("\nFirst Player is Win 🏆")
            self.score1 = self.score1 + 1

obj = stone_paper_scissor()
        
    