from test_engine import o
import random

class sample:
    def __init__(self,max):
        self.max=max
        self.n=0
        self.sorted=False
        self.some=[]

    def sampleInc(self,x):
        self.n+=1
        now=len(self.some)
        if now<self.max:
            self.sorted=False
            self.some.append(x)
        elif random.random()<now/self.n:
            self.sorted=False
            self.some[min(int(0.5+random.random()*now),len(self.some)-1)]=x
        return x

    def samplesorted(self):
        if not self.sorted:
            self.some.sort()
        return self.some

    def nth(self,n):
        s=self.samplesorted()
        return s[min(len(s),int(0.5+len(s)*n))]

    def nths(self,ns=[0.1,0.3,0.5,0.7,0.9]):
        out=[]
        for n in ns:
            out.append(self.nth(n))
        return out