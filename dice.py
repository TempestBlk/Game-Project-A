import random



class Dice():
    def roll(roll, logging=False, printing=False):
        amount = roll[0]
        die = roll[1]
        mod = roll[2]
        log = ""

        if printing:
            if mod >= 0:
                textMod = f"+{mod}"
            else:
                textMod = mod
            print(f"\t[Dice] Rolling {amount}d{die} {textMod}")

        total = 0
        roll_num = 0
        for _ in range(0, amount):
            roll_num += 1
            roll = random.randint(1, die)
            total += roll

            if logging:
                if log == "":
                    log += f"{roll}"
                else:
                    log += f"+{roll}"

            if printing:
                print(f"\tRoll {roll_num} -- {roll}/{die}")

        total += mod
        if logging:
            mod_sign = "+"
            if mod < 0:
                mod_sign = "-"
            log += f" ({mod_sign}{mod})"
            return total, log
        else:
            return total
