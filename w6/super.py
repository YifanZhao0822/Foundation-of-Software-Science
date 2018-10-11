from lib import *
from num import num
import re
from rows import data

# constants
global_enough=0.5
margin=1.05


class superv(data):
    def __init__(self,filename,**kwargs):
        super(superv,self).__init__(filename)
        self.goal=kwargs["goal"] if kwargs.get("goal") else len(self.rows[0])-1
        self.enough=kwargs["enough"] if kwargs.get("enough") else len(self.rows)**global_enough
        for c in self.indeps:
            if c in self.nums.keys():
                fyi("\n-- "+self.name[c]+" ---------")
                self.rows=ksort(c,self.rows)
                self.most=stop(c,self.rows)

                self.cuts(c,0,self.most,"|..")

        print(re.sub(r"\$","",cat(self.name)))
        dump(self.rows)


    def band(self,c,lo,hi):
        if lo==0:
            return ".."+str(self.rows[hi][c])
        elif hi==self.most:
            return str(self.rows[lo][c])+".."
        else:
            return str(self.rows[lo][c])+".."+str(self.rows[hi][c])

    def argmin(self,c,lo,hi):
        xl,xr=num(),num()
        yl,yr=num(),num()
        for i in range(lo,hi):
            xr.numInc(self.rows[i][c])
            yr.numInc(self.rows[i][self.goal])

        bestx=xr.sd
        besty=yr.sd
        mu=yr.mu
        cut=None
        if (hi-lo>2*self.enough):
            for i in range(lo,hi):
                x=self.rows[i][c]
                y=self.rows[i][self.goal]
                xl.numInc(x)
                xr.numDec(x)
                yl.numInc(y)
                yr.numDec(y)
                if xl.n>=self.enough and xr.n>=self.enough:
                    tempx=xl.numExpect(xl,xr)*margin
                    tempy = yl.numExpect(yl, yr) * margin
                    if xr.n<=3:
                        print(xr.n)
                    if tempx<bestx:
                        if tempy<besty:
                            cut,bestx,besty=i,tempx,tempy

        return cut,mu

    def cuts(self,c,lo,hi,pre):
        txt=pre+str(self.rows[lo][c])+".."+str(self.rows[hi][c])
        cut,mu=self.argmin(c,lo,hi)
        if cut:
            fyi(txt)
            self.cuts(c,lo,cut,pre+"|.. ")
            self.cuts(c,cut+1,hi,pre+"|.. ")
        else:
            s=self.band(c,lo,hi)
            fyi(txt+"==>"+str(int(100*mu)))
            for r in range(lo,hi):
                self.rows[r][c]=s



def stop(c, t):
    for i in range(len(t) - 1, -1, -1):
        if t[i][c] != "?":
            return i
    return 0