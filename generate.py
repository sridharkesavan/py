import random
"""
coin = random.choice(["heads", "tails"])
print(coin)


from random import choice
coin = choice(["heads", "tails"])
print(coin)



num = random.randint(1, 10)
print(num)

"""

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)

