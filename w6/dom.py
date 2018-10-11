from rows import data
from lib import *
import csv

#constants
samples=100

class dom(data):
    def dom(self,row1,row2):
        s1,s2,n=0,0,0

        for _ in enumerate(self.w):
            n+=1

        for _,(c,w) in enumerate(self.w.items()):
            a0=row1[c]
            b0=row2[c]
            a=self.nums[c].numNorm(a0)
            b = self.nums[c].numNorm(b0)
            s1-=10**(w*(a-b)/n)
            s2-=10**(w*(b-a)/n)

        return s1/n<s2/n

    def doms(self):
        n=samples
        c=len(self.name)
        header=cat(self.name)
        header+=">dom"
        print(header)
        for r1 in range(len(self.rows)):
            row1=self.rows[r1]
            row1[c]=0
            for s in range(n):
                row2=another(r1,self.rows)
                s=1/n if self.dom(row1,row2) else 0
                row1[c]+=s

        dump(self.rows)

        with open(self.filename[:-4]+"_dom.csv","w",newline="\n") as f:
            csvwriter=csv.writer(f)
            csvwriter.writerow(header.split(sep=","))
            for row in self.rows:
                csvwriter.writerow(row.values())



    def main_dom(self):
        self.doms()



