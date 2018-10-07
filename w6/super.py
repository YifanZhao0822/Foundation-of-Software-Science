from lib import *
from num import num
import re

# constants
global_enough=0.5
margin=1.05


def super(data,**kwargs):
    rows=data.rows
    goal=kwargs["goal"] if kwargs.get("goal") else len(rows[0])-1
    enough=kwargs["enough"] if kwargs.get("enough") else len(rows)**global_enough

    def band(c,lo,hi):
        if lo==0:
            return ".."+str(rows[hi][c])
        elif hi==most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])

    def argmin(c,lo,hi):
        xl,xr=num(),num()
        yl,yr=num(),num()
        for i in range(lo,hi):
            xr.numInc(rows[i][c])
            yr.numInc(rows[i][goal])

        bestx=xr.sd
        besty=yr.sd
        mu=yr.mu
        cut=None
        if (hi-lo>2*enough):
            for i in range(lo,hi):
                x=rows[i][c]
                y=rows[i][goal]
                xl.numInc(x)
                xr.numDec(x)
                yl.numInc(y)
                yr.numDec(y)
                if xl.n>=enough and xr.n>=enough:
                    tempx=xl.numExpect(xl,xr)*margin
                    tempy = yl.numExpect(yl, yr) * margin
                    if tempx<bestx:
                        if tempy<besty:
                            cut,bestx,besty=i,tempx,tempy

        return cut,mu

    def cuts(c,lo,hi,pre):
        txt=pre+str(rows[lo][c])+".."+str(rows[hi][c])
        cut,mu=argmin(c,lo,hi)
        if cut:
            fyi(txt)
            cuts(c,lo,cut,pre+"|.. ")
            cuts(c,cut+1,hi,pre+"|.. ")
        else:
            s=band(c,lo,hi)
            fyi(txt+"==>"+str(int(100*mu)))
            for r in range(lo,hi):
                rows[r][c]=s

    for c in data.indeps:
        if c in data.nums.keys():
            fyi("\n-- "+data.name[c]+" ---------")
            rows=ksort(c,rows)
            most=stop(c,rows)

            cuts(c,0,most,"|..")

    print(re.sub(r"%$","",cat(data.name)))
    dump(rows)

def stop(c, t):
    for i in range(len(t) - 1, -1, -1):
        if t[i][c] != "?":
            return i
    return 0