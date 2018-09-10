from num import num
from test_engine import o

@o.test
def num_test():
    n=num([4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])

    assert abs(n.mu-270.3)<0.001
    assert abs(n.sd-231.946)<0.001
    print("{0:f},{1:f}" .format(n.mu,n.sd))

if __name__=="__main__":
    o.report()