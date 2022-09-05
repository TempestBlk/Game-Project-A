import random

class Dice():
    def roll(roll):
        # assigning details of roll
        amount = roll[0]
        die = roll[1]
        mod = roll[2]

        total = 0
        for _ in range(0, amount):
            roll = random.randint(1, die)
            total += roll
        total += mod
        return total
    
    def print_roll(roll):
        # assigning details of roll
        amount = roll[0]
        die = roll[1]
        mod = roll[2]

        if mod >= 0:
            textMod = f"+{mod}"
        else:
            textMod = mod
        print(f"\nRolling {amount}d{die} {textMod}")
        total = 0
        for _ in range(0, amount):
            roll = random.randint(1, die)
            print(f"d6 = {roll}")
            total += roll
        total += mod
        return total