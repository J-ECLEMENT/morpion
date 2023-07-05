# besoin de cases, qui peuvent etre de type "X" "O" "" et une position (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)
class Case:
    def __init__(self, x, y , player):
        self.x = x
        self.y = y
        self.player = player

class Player:
    def __init__(self,type):
        self.type = type

class Plateau:
    def __init__(self, cases):
        self.cases= cases

    def print(self):
        print(self.cases[6].player + " | " + self.cases[7].player +  " | " + self.cases[8].player)
        print("---------")
        print(self.cases[3].player + " | " + self.cases[4].player +  " | " + self.cases[5].player)
        print("---------")
        print(self.cases[0].player + " | " + self.cases[1].player +  " | " + self.cases[2].player)
        

def menu():
    print("Welcome to TikTakToe from JEC")
    print("1-Player vs Player")
    print("2-Player vs CPU")
    print("3-CPU vs CPU")
    print("4-Quit")
    choise= input("Please make a choose : ")
    if choise == "1":
        pvp()
    elif choise == "2":
        pvu()
    elif choise == "3":
        uvu()
    else:
        quit()

def isWinning(plateau):
    if (plateau.cases[0].player == plateau.cases[1].player == plateau.cases[2].player) and plateau.cases[0].player != " ":
        return True
    elif (plateau.cases[3].player == plateau.cases[4].player == plateau.cases[5].player) and plateau.cases[3].player != " ":
        return True
    elif (plateau.cases[6].player == plateau.cases[7].player == plateau.cases[8].player) and plateau.cases[6].player != " ":
        return True
    elif (plateau.cases[0].player == plateau.cases[3].player == plateau.cases[6].player) and plateau.cases[0].player != " ":
        return True
    elif (plateau.cases[1].player == plateau.cases[4].player == plateau.cases[7].player) and plateau.cases[1].player != " ":
        return True
    elif (plateau.cases[2].player == plateau.cases[5].player == plateau.cases[8].player) and plateau.cases[2].player != " ":
        return True
    elif (plateau.cases[0].player == plateau.cases[4].player == plateau.cases[8].player) and plateau.cases[0].player != " ":
        return True
    elif (plateau.cases[2].player == plateau.cases[4].player == plateau.cases[6].player) and plateau.cases[2].player != " ":
        return True
    else:
        return False

def play(case, player, plateau):
    if plateau.cases[case].player == " " or player == " ":
        plateau.cases[case].player = player
        return plateau
    else:
        print("already use it")
        othercase=int(input("Chose a another case : "))-1
        while not (othercase<9 and othercase>-1):
                print("Please chose a number between 1 and 9")
                othercase = int(input("Player 1 chose a case : "))-1
        plateau = play(othercase, player, plateau)
        return plateau

def cpuPlay(cpu, player, plateau):
    listCaseScore=[3, 2, 3,
                   2, 4, 2,
                   3, 2, 3]
    i=0
    for case in plateau.cases:
        if not case.player == " ":
            listCaseScore[i] = 0
            i = i+1
        else:
            plateau =play(i, cpu, plateau)
            if isWinning(plateau):
                listCaseScore[i] = listCaseScore[i] + 1000
            plateau = play(i, " ", plateau)
            plateau = play(i, player, plateau)
            if isWinning(plateau):
                listCaseScore[i] = listCaseScore[i] + 500
            plateau = play(i, " ", plateau)
            # Special anti trap ! (cas particulier au le CPU se fait avoir car on anticipe son mouvement. 
            # Pas ouf comme code mais ça marche en mettant des malus, 
            # on pourrait faire un truc plus générique en mettant des masque sur la matrice de score par exemple
            # mais j'ai pas la foi de le faire : le resultat est le même notre CPU est invinsible)
            if plateau.cases[0].player == plateau.cases[8].player == player:
                listCaseScore[2] = listCaseScore[2] - 2
                listCaseScore[6] = listCaseScore[6] - 2
            if plateau.cases[2].player == plateau.cases[6].player == player:
                listCaseScore[0] = listCaseScore[0] - 2
                listCaseScore[8] = listCaseScore[8] - 2
            if plateau.cases[7].player == plateau.cases[5].player == player:
                listCaseScore[0] = listCaseScore[0] - 2
            if plateau.cases[7].player == plateau.cases[2].player == player:
                listCaseScore[0] = listCaseScore[0] - 2
            if plateau.cases[6].player == plateau.cases[5].player == player:
                listCaseScore[0] = listCaseScore[0] - 2
            i =i+1
    maxScore = max(listCaseScore)
    maxIndex = listCaseScore.index(maxScore)
    plateau = play(maxIndex, cpu, plateau)
    
    print("lets go")
    return plateau

def who_start():
    whoPlay = input("Chose who start (1 for player 1, 2 for player 2 or cpu) : ")
    if whoPlay == "1":
        return True
    elif whoPlay == "2":
        return False
    else :
        print("Please chose 1 or 2")
        who_start()

def explain_rule():
    print("7 | 8 | 9")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("1 | 2 | 3")

def pvp():
    listCase= [Case(0,0," "), Case(0,1," "), Case(0,2," "),
           Case(1,0," "), Case(1,1," "), Case(1,2," "),
           Case(2,0," "), Case(2,1," "), Case(2,2," ")]

    plateau = Plateau(listCase)
    player1 = Player("X")
    player2 = Player("O")
    par = 0

    whoplay=who_start()
    explain_rule()
    while par != 9:
        if whoplay:
            casePlay = int(input("Player 1 chose a case : "))-1
            while not (casePlay<9 and casePlay>-1):
                print("Please chose a number between 1 and 9")
                casePlay = int(input("Player 1 chose a case : "))-1
            plateau = play(casePlay, player1.type, plateau)
            plateau.print()
            if isWinning(plateau):
                print("Player 1 win !!")
                input()
                menu()
        if not whoplay:
            casePlay = int(input("Player 2 chose a case : "))-1
            while not (casePlay<9 and casePlay>-1):
                print("Please chose a number between 1 and 9")
                casePlay = int(input("Player 2 chose a case : "))-1
            plateau = play(casePlay, player2.type, plateau)
            plateau.print()
            if isWinning(plateau):
                print("Player 2 win !!")
                input()
                menu()
        if whoplay:
            whoplay = False
        else:
            whoplay = True
        par=par+1

    print("it's a draw")
    input()
    menu()
 

def pvu():
    listCase= [Case(0,0," "), Case(0,1," "), Case(0,2," "),
           Case(1,0," "), Case(1,1," "), Case(1,2," "),
           Case(2,0," "), Case(2,1," "), Case(2,2," ")]

    plateau = Plateau(listCase)
    player = Player("X")
    cpu = Player("O")
    par = 0
    whoplay=who_start()
    explain_rule()
    while par != 9:
        if whoplay:
            casePlay = int(input("Player chose a case : "))-1
            while not (casePlay<9 and casePlay>-1):
                print("Please chose a number between 1 and 9")
                casePlay = int(input("Player chose a case : "))-1
            plateau = play(casePlay, player.type, plateau)
            plateau.print()
            if isWinning(plateau):
                print("Player 1 win !!")
                input()
                menu()
        if not whoplay:
            print("CPU turn")
            plateau = cpuPlay(cpu.type, player.type, plateau)
            plateau.print()
            if isWinning(plateau):
                print("CPU win !!")
                input()
                menu()
        if whoplay:
            whoplay = False
        else:
            whoplay = True
        par=par+1
    print("it's a draw")
    input()
    menu()

def uvu():
    print("The CPU will try every possibility")
    p=0
    listCase= [Case(0,0," "), Case(0,1," "), Case(0,2," "),
           Case(1,0," "), Case(1,1," "), Case(1,2," "),
           Case(2,0," "), Case(2,1," "), Case(2,2," ")]

    plateau = Plateau(listCase)
    player = Player("X")
    cpu = Player("O")
    par = 0
    whoplay=True
    #cpu_enjoy(plateau, whoplay)
    print("it's a draw")
    menu()

menu()


# gagner le plus fort
# empeche l'adversaire de gagner au prochain tour
# trouver celui qui est le plus "fort"
