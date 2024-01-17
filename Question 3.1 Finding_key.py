
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total += (total < 13) - (total > 13) # the else function is changed to (total <13) - (total > 13) instead this will adjust the value based on the number 13 

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 1

print(total)