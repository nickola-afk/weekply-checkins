import random
cards = [
    ("k", "heart"), ("q", "heart"), ("j", "heart"), ("10_heart", "heart"), ("9_heart", "heart"),
    ("8_heart", "heart"), ("7_heart", "heart"), ("6_heart", "heart"), ("5_heart", "heart"), ("4_heart", "heart"),
    ("3_heart", "heart"), ("2_heart", "heart"), ("1_heart", "heart"),
    ("k_clubs", "clubs"), ("q_clubs", "clubs"), ("j_clubs", "clubs"), ("10_clubs", "clubs"),
    ("9_clubs", "clubs"), ("8_clubs", "clubs"), ("7_clubs", "clubs"), ("6_clubs", "clubs"), ("5_clubs", "clubs"), ("4_clubs", "clubs"),
    ("3_clubs", "clubs"), ("2_clubs", "clubs"), ("1_clubs", "clubs"),
    ("k_spades", "spades"), ("q_spades", "spades"), ("j_spades", "spades"), ("10_spades", "spades"),
    ("9_spades", "spades"), ("8_spades", "spades"), ("7_spades", "spades"), ("6_spades", "spades"), ("5_spades", "spades"), ("4_spades", "spades"),
    ("3_spades", "spades"), ("2_spades", "spades"), ("1_spades", "spades"),
    ("k_diamonds", "diamonds"), ("q_diamonds", "diamonds"), ("j_diamonds", "diamonds"), ("10_diamonds", "diamonds"),
    ("9_diamonds", "diamonds"), ("8_diamonds", "diamonds"), ("7_diamonds", "diamonds"), ("6_diamonds", "diamonds"), ("5_diamonds", "diamonds"), ("4_diamonds", "diamonds"),
    ("3_diamonds", "diamonds"), ("2_diamonds", "diamonds"), ("1_diamonds", "diamonds")
]

down1 = []
down2 = []
down3 = []
down4 = []
down5 = []
down6 = []
down7 = []

random_card = random.choice(cards)

def print_card_values(hand):
    return [card[0] for card in hand]

##print("Randomly selected card:", random_card)
##print("Card value (x):", random_card[0])
##print("Card suit (y):", random_card[1])

while len(down1) < 1:
    random_card = random.choice(cards)
    down1.append(random_card)
    cards.remove(random_card)
while len(down2) < 2:
    random_card = random.choice(cards)
    down2.append(random_card)
    cards.remove(random_card)
while len(down3) < 3:
    random_card = random.choice(cards)
    down3.append(random_card)
    cards.remove(random_card)
while len(down4) < 4:
    random_card = random.choice(cards)
    down4.append(random_card)
    cards.remove(random_card)
while len(down5) < 5:
    random_card = random.choice(cards)
    down5.append(random_card)
    cards.remove(random_card)
while len(down6) < 6:
    random_card = random.choice(cards)
    down6.append(random_card)
    cards.remove(random_card)
while len(down7) < 7:
    random_card = random.choice(cards)
    down7.append(random_card)
    cards.remove(random_card)

def draw():
    

print(down1)
print(down2)
print(down3)
print(down4)
print(down5)
print(down6)
print(down7)
print(" ")
print(" ")
print(" ")
print(" ")
print(cards)
