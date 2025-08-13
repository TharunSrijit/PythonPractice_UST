def sum(a,b):
    return a+b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
s1=sum(a,b)
print("NON LAMBDA:",s1)

ladd = lambda a,b:a+b
print("Sum using lambda",ladd(a,b))