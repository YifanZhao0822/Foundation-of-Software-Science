from test_engine import o
from sym import sym

@o.test
def sym_test():
    s=sym(['y','y','y','y','y','y','y','y','y',
	        'n','n','n','n','n'])

    assert abs(s.symEnt()-0.9403)<0.0001
    print(s.symEnt())

if __name__=="__main__":
    o.report()