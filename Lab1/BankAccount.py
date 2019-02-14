balance = 0
while 1:
    transaction = int(input("what would you like to do? 0:Deposit, 1:Withdraw ,2:Balance "))
    if transaction == 0:
        money = int(input("enter the amount: "))
        balance += money
    elif transaction == 1:
        money = int(input("enter the amount: "))
        balance -= money
    elif transaction == 2:
        print("your balance is $%d " %(balance))
    else: print("there was an error")