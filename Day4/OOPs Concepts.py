class classname1():
    def fn1(self):
        return a+b
    def fn2(self):
        return a-b
class classname2():
    def fn3(self):
        return a*b
    def fn4(self):
        return a/b

def main():
    obin1=classname1()
    obin2=classname2()
    print(obin1.fn1())
    print(obin1.fn2())

a,b=4,1
main()