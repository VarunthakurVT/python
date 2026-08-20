# from  random import choice
import random
# for _ in range(4):
#     coin=choice(["heads","tails"])
#     print(coin)
# number=random.randint(1,10)
# print(number)
cards=["king","queen","ace"]
random.shuffle(cards)
for card in cards:
    print(card)