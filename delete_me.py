def divide_by_zero(): # throws an exception by dividing by zero
    number = 32 #  amb(1 2 4) 8 16 32 64
    zero = 0
    print("Attempting to divide by 0")
    try:
        result = number / zero
    except:
        result = "CAN'T DIVIDE BY ZERO"
    print(f"Result of {result} successfully returned!")

# NOTE: names faye and i like
    # niamh (neev)          FV
    # saiorse (seer-sha)    FV
    # siobhan (sha-van)     FV
    # kal                   AZ
    # seer                  AZ
    # artyom (art-yom)      AZ
    # alec                  AZ
    # alekai (ale-kai)      AZ

# this is how a 'method' would be written w/out
class ThisIsAnObject():
    def this_does_something(self):
        thing = "done"
        return thing

# variable_A = ThisIsAnObject()
# variable_B = variable_A.this_does_something()
# print(variable_B)

def this_does_something():
    thing = "done"
    return thing

# variable_A = this_does_something()
# print(variable_A)