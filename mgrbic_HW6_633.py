import random
def diceprob(diceRolls):
    target_rolls = 0
    total_rolls = 0

    while target_rolls < 100:
        random_rolls = random.randrange(2,13)
        total_rolls += 1

        if random_rolls == diceRolls:
            target_rolls += 1
    print("It took", total_rolls, "to get to 100 rolls of", diceRolls)
