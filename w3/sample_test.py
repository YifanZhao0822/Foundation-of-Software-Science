from test_engine import o
from sample import sample
import random

@o.test
def sample_test():
    random.seed(5)
    s=[]
    for i in range(5):
        s.append(sample(2**(i+5)))
    for i in range(10000):
        y=random.random()
        for t in s:
            t.sampleInc(y)

    for t in s:
        print(t.max,t.nth(0.5))
        assert abs(t.nth(0.5)-0.5)<0.2


if __name__=="__main__":
    o.report()