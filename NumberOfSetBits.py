a = "before main Tis is sia a ai"
#b = list(a)
b = a.split(" ")
c = " ".join(b)
print(c)

dictT = {'a':1,'b':2}
for k,v in dictT.items():
    print(k,v)

class NumberCount():
    def __init__(self,num):
        if(num<0):
            print("Please enter positive number")
        else:
            self.num = num
            self.count = 0
    
    def getNumOfSetBits(self):
        if(self.num!=0):
            nDec = self.num-1
            self.num = self.num & nDec
            self.count +=1
            self.getNumOfSetBits()

if __name__== '__main__':
    n = 22
    coCount = NumberCount(n)
    coCount.getNumOfSetBits()
    print("Number of 1=",str(coCount.count))