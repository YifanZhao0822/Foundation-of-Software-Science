from lib import *
from num import num
import re

#constants
margin=1.05

def unsuper(data):
    rows=data.rows
    enough=len(rows)**0.5

    def band(c,lo,hi):
        if lo==0:
            return ".."+str(rows[hi][c])
        elif hi==most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])

    def argmin(c,lo,hi):
        if (hi-lo>2*enough):
            l,r=num(),num()
            for i in range(lo,hi):
                r.numInc(rows[i][c])
            best=r.sd
            cut=lo
            for i in range(lo,hi):
                x=rows[i][c]
                l.numInc(x)
                r.numInc(x)
                if l.n>=enough and r.n>=enough:
                    temp=l.numExpect(l,r)*margin
                    if temp<best:
                        cut,best=i,temp
            return cut
        else:
            return None

    def cuts(c,lo,hi,pre):
        txt=pre+str(rows[lo][c])+".."+str(rows[hi][c])
        cut=argmin(c,lo,hi)
        if cut:
            fyi(txt)
            cuts(c,lo,cut,pre+"|.. ")
            cuts(c,cut+1,hi,pre+"|.. ")
        else:
            b=band(c,lo,hi)
            fyi(txt+"("+b+")")
            for r in range(lo,hi):
                rows[r][c]=b

    for c in data.indeps:
        if c in data.nums.keys():
            rows=ksort(c,rows)
            most=stop(c,rows)
            fyi("\n-- "+data.name[c]+str(most)+"-------")
            cuts(c,1,most,"|.. ")

    print(re.sub(r"%$","",cat(data.name)))
    dump(rows)


def stop(c,t):
    for i in range(len(t)-1,-1,-1):
        if t[i][c]!="?":
            return i
    return 0