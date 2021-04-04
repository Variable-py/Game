import random

from colorama import Fore

print(Fore.CYAN+"{!} welcom to rock , paper , scissors game \n! for start send start \n! for info about creator send info \n! for help about game send help")
print(Fore.RED+"~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Pt = input().lower()
if Pt == "info":
     print(Fore.YELLOW+"Hello , i am Erfan. \n my telegram id : @SirVariable \n admin in pico hack and wasp team")
if Pt == "help":
     print(Fore.WHITE+"rock = sang \n paper = cughaz \n scissors = gheichyn \n for play use english words \n who wom 5 round of game is Winner \n you can quit the game with sending q or quit")
if Pt == "start":
  NP = input(Fore.YELLOW+"what is your Name ? : ")
  Player_1_wins = 0
  Player_2_wins = 0
  while Player_1_wins < 5 and Player_2_wins < 5:
    randomNumber = random.randint(0, 2)
    computerMove = None
    if randomNumber == 0:
      computerMove = "rock"
    elif randomNumber == 1:
      computerMove = "paper"
    elif randomNumber == 2:
      computerMove = "scissors"
    print(Fore.BLUE+f"{NP} score : {Player_1_wins} |  Computer score : {Player_2_wins}")
    Player_1 = input(Fore.MAGENTA+f" {NP} , Make your move : ").lower()
    print(Fore.MAGENTA+f" Computer move : {computerMove}")
    Player_2 = computerMove
    if Player_1 == "q" or Player_1 == "quit":
      break
      print(Fore.RED+"game finished")
    if Player_1 == Player_2:
      print(Fore.YELLOW+"thats a tie ...")
    elif Player_1 == "rock":
      if Player_2 == "scissors":
          print(Fore.GREEN+f"{NP} wins!....")
          Player_1_wins += 1
      elif Player_2 == "paper":
          print(Fore.RED+"Computer wins!...")
          Player_2_wins += 1
    elif Player_1 == "paper":
      if Player_2 == "rock":
          print(Fore.GREEN+f"{NP} wins!...")
          Player_1_wins += 1
      elif Player_2 == "scissors":
          print(Fore.RED+"Computer wins!...")
          Player_2_wins += 1
    elif Player_1 == "scissors":
      if Player_2 == "paper":
          print(Fore.GREEN+f"{NP} wins!...")
          Player_1_wins += 1
      elif Player_2 == "rock":
          print(Fore.RED+"Computer wins!...")
          Player_2_wins += 1
    else:
      print(Fore.BLUE+"something went wrong ....")
  print(Fore.CYAN+f"GAME FINISHED \n {NP} score : {Player_1_wins} |  Computer score : {Player_2_wins}")

#Coded by : @SirVariable