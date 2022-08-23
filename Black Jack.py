from msilib.schema import RadioButton
import random


def random_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_cards = []
comp_cards = []

for _ in range(2):
    user_cards.append(random_card)
    comp_cards.append(random_card)

def score(cards):
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user,comp):
    if user ==comp:
        return 'draw'
    elif user == 0:
        return 'comp wins'
    elif comp == 0:
        return 'you win'
    elif comp > 21:
        return ' you win'
    elif user > 21:
        return 'comp win'
    elif user > comp:
        return ' you win'
    elif comp > user:
        return 'comp win'

gameOver = False

while not gameOver:
    user_score = score(user_cards)
    comp_cards = score(comp_cards)
    print(f"user score")
    print(f"comp_score")
    if comp_cards <17:
        comp_cards.append(random_card)
    
    