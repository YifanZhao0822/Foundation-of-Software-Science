from w4 import data
from test_engine import o

@o.test
def weather():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/weather.csv"
    t=data(filename)

    print("\t\tn\tmode\tfrequency")
    for col,obj in enumerate(t.syms):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mode,obj.most))
    print("\t\tn\tmu\tsd")
    for col,obj in enumerate(t.nums):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mu,obj.sd))
    print(".")

@o.test
def weatherlong():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/weatherlong.csv"
    t=data(filename)
    print("\t\tn\tmode\tfrequency")
    for col,obj in enumerate(t.syms):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mode,obj.most))
    print("\t\tn\tmu\tsd")
    for col,obj in enumerate(t.nums):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mu,obj.sd))

@o.test
def auto():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w4/auto.csv"
    t=data(filename)
    print("\t\tn\tmode\tfrequency")
    for col,obj in enumerate(t.syms):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mode,obj.most))
    print("\t\tn\tmu\tsd")
    for col,obj in enumerate(t.nums):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(col,t.name[col],obj.n,obj.mu,obj.sd))


if __name__=="__main__":
    o.report()