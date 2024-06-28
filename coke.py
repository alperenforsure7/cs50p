#5 cent ,10 cent, 25 cent, cent are valid

cost = 50
due = cost


while due > 0:
    print("Amount due:", int(due))
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin

    else:
        print("Only insert 25, 10 or 5 cents")
    
    
if due < 0:
    due = -due

print("Change Owned:", str(due))
