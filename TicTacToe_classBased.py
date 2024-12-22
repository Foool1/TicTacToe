import random

class Board:
    def __init__(self):
        pass
    
    def display(self, table):
        for i in range(3):
            for j in range(3):
                print(f"|{table[i][j]}", end="")
            print("|", end="")
            print("")

    def showBoard(self):
        x = 0
        for i in range(3):
            for j in range(3):
                print(f"|{x}", end="")
                x+=1
            print("|", end="")
            print("")

    def ai(self, table):
        x = random.randint(0,2)
        y = random.randint(0,2)
        while table[x][y] != ' ':
            x = random.randint(0,2)
            y = random.randint(0,2)
        table[x][y] = 'X'

    def winner(self, table):
#row:
        result = ""
        for i in range(3):
            for j in range(3):
                result += table[i][j]
            if result == "OOO":
                return True
            elif result == "XXX":
                return False
            result = ""
#column:
        result = ""
        for i in range(3):
            for j in range(3):
                result += table[j][i]
            if result == "OOO":
                return True
            elif result =="XXX":
                return False
            result = ""
#diagonal
        result = ""
        for i in range(3):
            result += table[i][i]
        if result == "OOO":
            return True
        elif result == "XXX":
            return False
        result = ""
        for i in range(3):
            result += table[i][2-i]
        if result == "OOO":
            return True
        elif result == "XXX":
            return False
        result = ""

    def draw(self, table):
        for i in range(3):
            for j in range(3):
                if table[i][j] == ' ':
                    return False
        return True

class Game:
    def __init__(self):
        self.table = [[' '] * 3 for _ in range(3)]
        self.board = Board()
    
    def game(self):
        while any(' ' in row for row in self.table):
            print("press the number where u want to put your \"O\" character: ", end="")
            check = 1
            while check == 1:
                player = 9
                while player not in range(9):
                    player = int(input())
                    if player not in range(9):
                        print("You enter wrong input, try again")

                fdigit = player / 3
                sdigit = player % 3
                if self.table[int(fdigit)][int(sdigit)] == ' ':
                    self.table[int(fdigit)][int(sdigit)] = "O"
                    check = 0
                else:
                    print("This possition is taken, try again")
            self.board.display(self.table)
            if Board().winner(self.table) == True:
                print("You won!")
                return True
            elif Board().winner(self.table) == False:
                print("You lost!")
                return False
            if Board().draw(self.table) == True:
                print("It is a draw!")
                return True        
            print("AI move: ")
            Board().ai(self.table)
            self.board.display(self.table)
            if Board().winner(self.table) == True:
                print("You won!")
                return True
            elif Board().winner(self.table) == False:
                print("You lost!")
                return False

print("Welcome in TicTacToe game, thats how positions on board looks like: ")

Board().showBoard()
Game().game()
