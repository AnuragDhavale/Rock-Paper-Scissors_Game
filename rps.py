import random

a = ["Rock", "Scissors", "Paper"]

while True:  # To repeat the game after 5 rounds
    ccount = 0  # Computer count for score
    ucount = 0  # User count for score
    
    uc = int(input('''
Game Start 
1 Yes
2 No | Exit

'''))
    
    if uc == 1:
        for i in range(1, 6):  # FIVE rounds of the game
            userinput = int(input('''
1 Rock
2 Scissors
3 Paper
         
'''))
            if userinput == 1:
                uchoice = "Rock"  # uchoice = User Choice
            elif userinput == 2:
                uchoice = "Scissors"
            elif userinput == 3:
                uchoice = "Paper"
            else:
                print("Invalid input, please choose 1, 2, or 3")
                continue

            Cchoice = random.choice(a)  # Cchoice = Computer Choice which is Random
            print("Computer Value=", Cchoice)
            print("User Value=", uchoice)
            
            if Cchoice == uchoice:
                print("Game Draw")
                ccount=ccount+1
                ucount=ucount+1
                
                #User Winning Case
            elif (uchoice == "Rock" and Cchoice == "Scissors") or \
                 (uchoice == "Paper" and Cchoice == "Rock") or \
                 (uchoice == "Scissors" and Cchoice == "Paper"):
                print("You Win")
                ucount=ucount+1
            
            else:
                print("Computer Win")
                ccount += 1

        if ucount==ccount:
            print("Final Game Draw")
            print("User Score=",ucount)
            print("Computer Score=",ccount)

        elif ucount>ccount:
            print("YOU WIN !!")
            print("User Score=",ucount)
            print("Computer Score=",ccount)

        else:
            print("COMPUTER WIN")
            print("Computer Score=",ccount)
            print("User Score=",ucount)


    else:
        break
