def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def main():
    print(add(a,b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))

a,b=4,1
if __name__=='__main__':
    main()
else:
    print(add(a,b))