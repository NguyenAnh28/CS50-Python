
# Ask user for input
# Only except '5', '10', '25'
amount_due = 50
print(f"Amount due: {amount_due}")

# Calculate new amount
while amount_due > 0:
    coin = int(input("Insert coin: "))
    if coin in (5, 10, 25):
        amount_due = amount_due - coin
        if amount_due > 0:
            print(f"Amount due: {amount_due}")
        else:
            break
    if amount_due == 0:
        break
        
print("Change owed: 0")