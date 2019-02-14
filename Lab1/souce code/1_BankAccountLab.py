totalAmount = 0
print("Welcome to the bank, would you like to deposit or withdraw? Ctrl-D/command-D( Mac ) when you're done")


def usrdecision():
    """Function that'll allow the user to continuously give input that would return as a string"""
    inputs = []
    while True:
        try:
            decision = input().lower()
        except EOFError: break
        inputs.append(decision)
    return inputs
usrInput = usrdecision()

for word in usrInput:
    action = word.split()
    if action[0] == "deposit":
        amount = float(action[1])
        totalAmount = totalAmount + amount
    elif action[0]== "withdraw":
        amount = float(action[1])
        totalAmount = totalAmount - amount

print("Total amount is ${0}".format(totalAmount))
