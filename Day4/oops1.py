class addsub():
    def add(self):
        return a+b
    def sub(self):
        return a-b
class muldiv():
    def mul(self):
        return a*b
    def div(self):
        return a/b

def main():
    adsu=addsub()
    mudi=muldiv()
    print(adsu.add())
    print(mudi.mul())

a,b=4,1
if __name__=='__main__':
    main()
else:
    adsu=addsub()
    mudi=muldiv()
    print(adsu.sub())
    print(mudi.div())