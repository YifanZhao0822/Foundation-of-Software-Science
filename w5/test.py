from dom import dom
from unsuper import unsuper
from rows import data
from test_engine import o

@o.test
def weatherlong():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w5/weatherlong.csv"
    t1=dom(filename)
    t1.main_dom()

@o.test
def auto():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w5/auto.csv"
    t2=dom(filename)
    t2.main_dom()

@o.test
def unsuper_test():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w5/weatherlong.csv"
    unsuper(data(filename))

if __name__=="__main__":
    o.report()