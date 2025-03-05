result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count = 0
for i in result:
    if i == "heads":
        count += 1
        
print(f"Head Count: {count}")