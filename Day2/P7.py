'''def rev(a):
    return a[::-1]
s="Hello"
a=rev(s)
print(a)'''

def rev(a):
    l=[]
    for i in range(len(a)-1,-1,-1):
        l.append(a[i])

    for i in range(len(l)):
        print(l[i],end="")

a=input("Enter a string: ")
print(rev(a))
