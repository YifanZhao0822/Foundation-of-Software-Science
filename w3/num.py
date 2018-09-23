from sample import sample

inf=float("Inf")
epsilon=10**(-32)

class num:
    def __init__(self,max=512,nums=[],func=lambda x:x):
        self.max=max
        self.n=0
        self.mu=0
        self.m2=0
        self.sd=0
        self.lo=inf
        self.hi=-inf
        self.w=1
        self._some=sample(self.max)
        for x in nums:
            self.numInc(func(x))


    def numInc(self,x):
        if x=="?": return x
        self.n+=1
        self._some.sampleInc(x)
        d=x-self.mu
        self.mu+=d/self.n
        self.m2+=d*(x-self.mu)
        if x>self.hi: self.hi=x
        if x<self.lo: self.lo=x
        if self.n>1:
            self.sd=(self.m2/(self.n-1+epsilon))**0.5
        return x

    def numDec(self,x):
        if x == "?"or self.n==1: return x
        self.n-=1
        d=x-self.mu
        self.mu-=d/self.n
        self.m2-=d*(d-self.mu)
        if self.n>1:
            self.sd=(self.m2/(self.n-1+epsilon))**0.5
        return x

    def numNorm(self,x):
        return 0.5 if x=="?" else (x-self.lo)/(self.hi-self.lo+epsilon)

    def numExpect(self,i,j):
        n=i.n+j.n+epsilon
        return i.n/n*i.sd+j.n/n*j.sd
