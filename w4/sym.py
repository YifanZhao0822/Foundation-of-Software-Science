from collections import Counter
from math import log

class sym:
    def __init__(self,syms,func=lambda x:x):
        self.counts = Counter()
        self.mode=None
        self.most=0
        self.n=0
        self._ent=None
        self.syms=syms

        for x in self.syms:
            self.symInc(func(x))


    def symInc(self,x):
        if x=="?": return x
        self._ent=None
        self.n+=1
        old=self.counts[x]
        new=old+1 if old else 1
        self.counts[x]=new
        if new>self.most:
            self.most,self.mode=new,x
        return x

    def symDec(self,x):
        self._ent=None
        self.n-=1
        self.counts[x]-=1
        return x

    def symEnt(self):
        if not self._ent:
            self._ent=0
            for n in list(self.counts.values()):
                p=n/self.n
                self._ent-=p*log(p,2)
        return self._ent