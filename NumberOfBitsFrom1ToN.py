import math
class getAllCounts():
    def __init__(self,n):
        self.n = n
        self.count = 0

    def getMaxIvalue(self):
        return math.ceil(math.log(self.n,2))

    def getCount(self):
        maxCtr = self.getMaxIvalue()
        for i in range(1,maxCtr):
            self.count += 

if __name__=='__main__':
    obj = getAllCounts(9)
    i = obj.getMaxIvalue()
    print("Max power of 2 = {0:d}".format(i))