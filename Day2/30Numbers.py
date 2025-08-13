
for i in range(1,30):

    if (i % 4 == 0 and i % 10 == 0):
        print()
        continue
    elif (i%4==0):
        continue
    elif (i % 10 == 0):
        print(i, end=" \n")

    else:
        print(i,end=" - ")
i=i+1
print(i,end="   ")