import random

def play():   
  
  dict = {
    "r" : """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "p" : """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "s" : """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
  }
  comp = random.choice( ["r", "p", "s"])
  user = input("Choose 'r' for rock 'p' for paper 's' for scissors: ").lower()
  print(f"user has picked {dict[user]}\nComputer has picked {dict[comp]}")  
  if user=="r" or user=="p" or user=="s":
    if user == comp:  
      return "Tie"
    if is_win(user,comp):
      return "Yay! You win"
    return "You lose..!"
  else:
    print("Choose 'r' for rock 'p' for paper 's' for scissors")

def is_win(player, opponent):
  if (player=="r" and opponent=="s") or (player=="s" and opponent=="p") or (player=="p" and opponent=="r"):
    return True


print(play())

  