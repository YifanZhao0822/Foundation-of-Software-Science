from num import num
from sym import sym
import re


class data:

    def __init__(self,filename):
        self.w={}
        self.syms={}
        self.nums={}
        self.Class=None
        self.rows=[]
        self.name=[]
        self._use=[]
        self.indeps=[]
        self.filename=filename



    def indep(self,current):
        return not self.w[current] and self.Class!=current

    def dep(self,current):
        return not self.indep(current)

    def header(self,cells):     #w
        for c0,x in enumerate(cells):
            if not re.match(r"\?",x):
               c=len(self._use)
               self._use.append(c0)
               self.name.append(x)
               if re.match(r"[<>\$]",x):
                   self.nums[c]=num()
               else:
                   self.syms[c]=sym([])
               if re.match("<",x):
                   self.w[c]=-1
               elif re.match(">",x):
                   self.w[c]=1
               elif re.match("!",x):
                    self.Class=c
               else:
                   self.indeps.append(c)
        return True


    def row(self,cells):
        r=len(self.rows)
        self.rows.append({})
        for c,c0 in enumerate(self._use):
            x=cells[c0]
            if not x=="?":
                if c in self.nums.keys():
                    x=float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)

            self.rows[r][c]=x
        return True


    def rows1(self):
        with open(self.filename,"r+") as f:
            first=True
            for line in f:
                line=re.sub(r"[\t\r\n ]","",line)
                line=re.sub(r"#.*","",line)
                cells=line.split(",")
                if len(cells)>0:
                    if first:
                        self.header(cells)
                    else:
                        self.row(cells)
                first=False

'''
    def rows(self,file):
        return self.rows1(file)#input
'''