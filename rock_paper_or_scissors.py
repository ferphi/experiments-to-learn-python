import random
Draws=0
Player_win=0
Machine_win=0
Options_list=["Rock","Paper","Scissors"]  
while True:
    Question=input("Do you want to play rock, paper or scissors vs the machine? Press 1 followed by enter to indicate YES or 0 followed by enter to indicate NO: ")
    if Question=="1" or Question=="0":
        if Question=="1":
            print()
            print("Explaining the rules of the game:")
            print()
            print("-The rock crushes the scissors. (Win the rock)")
            print("-The scissors cut the paper. (Scissors wins)")
            print("-The paper wraps the rock. (Win the role)")
            print("-Two players choose the same item. (It's a tie and it's played again)")
            print("-THE FIRST TO REACH 3 WINS IS THE WINNER")
            print()
            print("Options:")
            print(Options_list)
            while True:
                print()
                option=input("Enter your option and press enter: ")
                option=option.strip()
                option=option.capitalize()
                if option in Options_list:
                    option=Options_list.index(option)+1              
                    machine_option = random.randint(1, 3)
                    print("The machine selected:",Options_list[machine_option-1])
                    if abs(machine_option-option)==0:
                        print("it's a draw")
                        Draws+=1
                    elif abs(machine_option-option)==1:
                        if max(machine_option,option)==option:
                            print("You win, the machine loses")
                            Player_win+=1
                            if Player_win==3:
                               break
                        else:
                            print("You lose, the machine wins")
                            Machine_win+=1
                            if Machine_win==3:
                                break
                    else:
                        if min(machine_option,option)==option:
                            print("You win, the machine loses")
                            Player_win+=1
                            if Player_win==3:
                                break
                        else:
                            print("You lose, the machine wins")
                            Machine_win+=1
                            if Machine_win==3:
                                break
                else:
                    print("You did not enter a valid option, please try again:") 
            print()
            print("Draws: ",Draws)
            print("Number of times the player won: ",Player_win)
            print("Number of times the machine won: ",Machine_win)         
        else:
            print("I leave the game")
            break
            exit
    else:
        print("You did not choose a correct option, try again:")