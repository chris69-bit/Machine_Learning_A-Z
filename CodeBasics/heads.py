#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

#count = 0
#for i in result:
#    if i == "heads":
#        count += 1
        
#print(f"Head Count: {count}")

expense_list = [2340, 2500, 2100, 3100, 2980]

amount = int(input("Enter the amount: "))

for i in expense_list:
    if i == amount:
        print("Amount found")
        break
    else:
        print("Amount not found")
        break