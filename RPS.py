#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
  while playAgain == "Y": 
    #User can play as many games as they wish.
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])
    #Prompt the user for their RPS selection
    user = input("Pick your selection (R, P, S): ")
    #Determine winner and state what happened to the user
    if computer == "R":
      print("computer chose Rock")
    elif computer == "P":
      print("computer chose Paper ")
    else:
      print("computer chose Scissors")

    if user == computer:
        print("It's a tie!")
        ties += 1
    elif (user == "R" and computer == "S") or \
          (user == "P" and computer == "R") or \
          (user == "S" and computer == "P"):
        print("You win!")
        wins += 1
    else:
        print("Computer wins!")
        losses += 1
    #Ask the user if they would like to play again.
    playAgain = input("play again? (Y/N): ")
    
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
