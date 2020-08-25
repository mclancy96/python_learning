from random import random

def flip():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip())