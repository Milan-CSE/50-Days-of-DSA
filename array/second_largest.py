ar = [4,563,1,263,263,6,76,563,-1,-2]

largest = ar[0]
s_largest = -1
for i in ar:
    if i>largest:
        largest = i

for i in ar:
    if i>s_largest and i<largest:
        s_largest = i

print(s_largest)