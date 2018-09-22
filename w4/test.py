from w4 import data
from test_engine import o

@o.test
def weather():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/weather.csv"
    t=data(filename)
    t.rows1()
    print("\t\tn\tmode\tfrequency")
    for col in t.syms:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],t.syms[col].n,t.syms[col].mode,t.syms[col].most))
    print("\t\tn\tmu\tsd")
    for col in t.nums:
        print("{0}\t{1}\t{2}\t{3:.3f}\t{4:.3f}".format(col,t.name[col],t.nums[col].n,t.nums[col].mu,t.nums[col].sd))

@o.test
def weatherlong():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/weatherlong.csv"
    t=data(filename)
    t.rows1()
    print("\t\tn\tmode\tfrequency")
    for col in t.syms:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],t.syms[col].n,t.syms[col].mode,t.syms[col].most))
    print("\t\tn\tmu\tsd")
    for col in t.nums:
        print("{0}\t{1}\t{2}\t{3:.3f}\t{4:.3f}".format(col,t.name[col],t.nums[col].n,t.nums[col].mu,t.nums[col].sd))

@o.test
def auto():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/auto.csv"
    t=data(filename)
    t.rows1()
    print("\t\t\tn\tmode\tfrequency")
    for col in t.syms:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],t.syms[col].n,t.syms[col].mode,t.syms[col].most))
    print("\t\t\tn\tmu\tsd")
    for col in t.nums:
        print("{0}\t{1}\t{2}\t{3:.3f}\t{4:.3f}".format(col,t.name[col],t.nums[col].n,t.nums[col].mu,t.nums[col].sd))


if __name__=="__main__":
    o.report()