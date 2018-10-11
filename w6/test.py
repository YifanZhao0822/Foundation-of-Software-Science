from dom import dom
from super import superv
from rows import data
from test_engine import o

@o.test
def weatherlong():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w6/weatherlong_dom.csv"
    superv(filename)

@o.test
def auto():
    filename="D:/academic/Software_Sciences/Foundation-of-Software-Science/w6/auto_dom.csv"
    superv(filename)

if __name__=="__main__":
    o.report()