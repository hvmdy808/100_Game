# File : CS112_A1_T2_Game1_20230126
# Purpose : Tow players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author : Hamdy Mohamed Hamdy Abdelazim
# ID : 20230126


# That function asks the player to enter a number if the player chooses a character
def is_there_a_non_number_value(value):
      while True:
            if(value.isdigit() ) :
                return (value)
                
            else:
                value= input("Please, enter a positive intger number!")

            

# Welcoming message for the players
print("Hello! Welcome to 100 game!")

# Asking the players for their names
first_player_name= str(input("Enter a name for first player:"))
second_player_name= str(input("Enter a name for second playe:r"))
valid_numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 ]            
print(" 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 are the valid numbers!")
# The game starts from 0 /// The counter decides the winner
counter=0
result=0

while True:          
               
                    print("Now you have", result, "!")
                    i = int(is_there_a_non_number_value(input(f"Enter a number from 1 to 10 to add it to {result}:")))
                    
                    # IF a player adds a wrong number, the program ask them to try again with a valid number 
                    while i not in valid_numbers:
                        i = int(is_there_a_non_number_value(input("Please, try again with a valid number:")))   
                    
                    while result+i>100:
                          i = int(is_there_a_non_number_value(input("Please, try again with a smaller valid number:")))
                    
                    result= result+i
                    counter=counter+1   
                    if result==100:
                        print("Game over!")
                        
                        # If the first player adds a valid number fot their first time, the counter turns from 0 to 1. 
                        # If the second player adds a valid number fot their first time, the counter turns from 1 to 2.
                        # So if the counter is odd, then the player who played last is the first player and supposed to be the winner.
                        if counter%2!=0:
                            print(first_player_name, "is the winner!")
                            break
                        
                        # And if the counter is even, then the player who played last is the second player and supposed to be the winner
                        if counter%2==0:
                            print(second_player_name, "is the winner")
                            break