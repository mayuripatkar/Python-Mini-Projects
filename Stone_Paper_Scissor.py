import random
options = ["Stone","Paper","Scissor"]

pc = options[random.randint(0,2)]
player = False

while player == False:
    player = input("Stone,Paper,Scissor?")
    if player == pc:
        print(player,"versus",pc,"\nIt's a tie!")
    elif player == "Stone":
        if pc == "Scissor":
            print(player,"versus",pc,"\nYou won as ",player,"breaks ",pc)
        else:
            print(player,"versus",pc,"\nYou lost as ",pc,"wraps",player)
    elif player == "Paper":
        if pc == "Scissor":
            print(player,"versus",pc,"\nYou lost as ",pc,"cuts",player)
        else:
            print(player,"versus",pc,"\nYou won as ",player,"wraps ",pc)
    elif player == "Scissor":
        if pc == "Paper" :
            print(player,"versus",pc,"\nYou won as ",player,"cuts",pc)
        else:
            print(player,"versus",pc,"\nYou lost as ",pc,"breaks",player)
    else:
        print(player,"versus",pc,"\nInvalid Input")
    player = False
    pc = options[random.randint(0,2)]
