import re,traceback

class hw1:
    y=n=0
    @staticmethod
    def report():
        print("\n pass= %s, fail= %s, %%pass= %s%%" % (hw1.y,hw1.n,round(hw1.y*100/(hw1.y+hw1.n+0.0001))))

    @staticmethod
    def test(f):
      try:
         print("\n------------|%s|------------" % f.__name__)
         if f.__doc__:
             print("# "+re.sub(r'\n[ \t]*',"\n",f.__doc__))
         f()
         print("pass")
         hw1.y+=1
      except:
         hw1.n+=1
         print(traceback.format_exc())
      return f

@hw1.test
def indent():
    # i looped in a matrix for testing the structure and continued lines
    for i in [[1, 2, 3],\
               [4, 5, 6],
               [7, 8, 9]]:
        for j in [1, 2, 3]:
            print(j)
            print(i)
        print(i)
    print("Done looping")

@hw1.test
def module():
    import urllib
    from matplotlib.mlab import PCA
    import numpy as np
    import matplotlib.pyplot as plt
    pca=PCA(np.array([[2,3],[4,5]]))
    print(pca)

@hw1.test
def issue_27():
    real=5/2
    integer=5//2
    print("Real number division: 5/2=%.1f" % real)
    print("Integer division: 5/2=%d" % integer)

@hw1.test
def function():
    def apply_to_two(f,a=0,b=0):
        return f(2),b
    print(apply_to_two(lambda x:x*2,b=3))

@hw1.test
def strings():
    print("Double qouted string")
    print('Single qouted string')
    print('''Triple single qouted
    multiline string''')
    print("""Triple double qouted 
    multiline string""")

@hw1.test
def exceptions():
    try:
        print(6/0)
    except ZeroDivisionError:
        print("Cannot be divided by zero")

@hw1.test
def lists():
    list1=range(10)
    list2=range(10,20)
    list3=[list1,list2]
    print("The length of list3 is %d" % len(list3))
    print("list3[0][0]=%d" % list3[0][0])
    print("list3[0][2:8] is %s" % list(list3[0][2:8]))
    print("list3[0][2:] is %s" % list(list3[0][2:]))
    print("list3[0][:8] is %s" % list(list3[0][:8]))
    print("list3[0][:-1] is %s" % list(list3[0][:-1]))
    i=2
    print("i is in list1: %s" % bool(i in list1))
    list4=[]
    list4.extend(list1)
    list4.append(10)
    print("list4 is %s" % list4)
    list5=list4+list(list2)
    print("list5 is %s" % list5)
    x,y=[0,1]
    _,z=[0,1]
    print("y==z is %s" % bool(y==z))

@hw1.test
def tuples():
    toy_tuple=(1,2)
    try:
        toy_tuple[1]=5
    except TypeError:
        print("Tuples can not be modified")
    def product_and_power(x,y):
        return x*y,x**y
    pp=product_and_power(2,3)
    print("2*3 and 2^3 is {0:d}, {1:d}".format(pp[0],pp[1]))

@hw1.test
def dictionaries():
    new_dict={"name": "Yifan","course": "FSS"}
    try:
        time=new_dict["time"]
    except KeyError:
        print("No key named time")
    print("There is key named name: %s" % bool("name" in new_dict))
    print("get method test: %d" % new_dict.get("time",0))
    new_dict["time"]="TT0430p"
    print("The length of new_dict: %d" % len(new_dict))
    keys=new_dict.keys()
    values=new_dict.values()
    items=new_dict.items()
    print("The keys of new_dict: %s" % keys)
    print("The values of new_dict: %s" % values)
    print("The items of new_dict: %s" % items)

@hw1.test
def defaultdicts():
    from collections import defaultdict
    dd_test=defaultdict(str)
    dd_test["key"]+="The defaultdict works well."
    print(dd_test)

@hw1.test
def counter():
    from collections import Counter
    StdtID=Counter([2,0,0,2,6,2,0,2,3])
    print(StdtID)
    print(StdtID.most_common(2))

@hw1.test
def sets():
    s=set()
    s.add("Foundation")
    s.add("Software")
    s.add("Science")
    s.add("Science")
    print("Sets only have distinct entries: %d" % len(s))
    print("in test: %s" % bool("of" in s))

@hw1.test
def ctrl_flow():
    for i in range(10):
        flag=False if i<=8 else True
        if flag:
            print("Cease loop")
            break
        else:
            print("Processing loop no. %d" % (i+1))
            continue

@hw1.test
def truthiness():
    if False or None or [] or {} or "" or set() or 0 or 0.0:
        print("Oops! Something must be wrong")
    else:
        print("They are all falsy")

    if all([True,1,"arimasu"]):
        print("all works well")
    if any([True,0,'']):
        print("any works well")

@hw1.test
def sorting():
    s=[10,9,8,7,6]
    s.sort()
    print(s)
    r=sorted(s,reverse=True)
    print(r)

@hw1.test
def list_cprhs():
    odds=[x for x in range(10) if x%2==1]
    squares=[x*x for x in range(10)]
    odd_squares=[x*x for x in odds]
    cube_dict={x:pow(x,3) for x in range(10)}
    cub_set={pow(x,3) for x in range(10)}
    ones=[1 for _ in range(10)]
    pairs=[(x,y) for x in range(10) for y in range(5)]
    increasing_pairs=[(x,y) for x in range(5) for y in range(x+1,10)]
    if odds and squares and odd_squares and cube_dict and cub_set\
            and ones and pairs and increasing_pairs:
        print("They all work well")

@hw1.test
def iter_gene():
    def yield_test(n):
        i=0
        while i<n:
            yield i
            i+=1

    for x in yield_test(10):
        print(x)
    # The keyword yield is like a return
    # But the function will run right after the line of yield, which is different from return

    lazy_odds_below_20=(i for i in yield_test(20) if i%2==1)
    print(lazy_odds_below_20)
    # Since the generators are mainly about save unnecessary memories,
    # it is relatively harder than others to demonstrate that I have understood.

@hw1.test
def randomness():
    import random
    unif_rand=random.random()
    print("Uniformly distrbuted number: %f" % unif_rand)
    random.seed(15)
    seed_rand1=random.random()
    random.seed(15)
    seed_rand2 = random.random()
    print("Since the seed keeps unchanged, the random number also: %s" % bool(seed_rand1==seed_rand2))
    rand_range=random.randrange(10)
    print("The random number is in range(10): %s" % bool(rand_range in range(10)))
    zero_to_nine=[x for x in range(10)] #since the range in Py3 is lazy, we need to do this way
    random.shuffle(zero_to_nine)
    print(zero_to_nine)
    pickup=random.choice(zero_to_nine)
    print("Randomly picked up number: %d" % pickup)
    w_o_re=random.sample(zero_to_nine,2)
    print("Sample without replacement: %s" % w_o_re)
    w_re=[random.choice(zero_to_nine) for _ in range(2)]
    print("Sample with replacement: %s" % w_re)

@hw1.test
def regex():
    import re
    print(all([not re.match("a","leopard"),
               re.search("a","leopard"),
               not re.search("a","tiger"),
               3==len(re.split("[ie]","tiger")),
               "C-PO"==re.sub("[0-9]","-","C3PO")
               ]))
    '''
    I once used regular expressions in a project searching some texts in some html files.
    Maybe its so tricky or maybe I am too dull(hahahahah:D) that I would rather say regex is an art than a skill.
    '''

@hw1.test
def obj_orient():
    class my_set:

        def __init__(self,values=None):
            self.dict={}
            if values:
                for value in values:
                    self.add(value)

        def __repre__(self):
            return "Set's string representation: "+str(self.dict.keys())

        def add(self,value):
            self.dict[value]=True

        def contains(self,value):
            return value in self.dict

        def remove(self,value):
            try:
                del self.dict[value]
            except KeyError:
                print("There is no such entry in the set!")

    set_obj=my_set([1,2])
    set_obj.add(3)
    print("The set contains 3: %s" % set_obj.contains(3))
    set_obj.remove(4)

@hw1.test
def func_tools():

    from functools import partial,reduce
    #partial
    def exp(x,y):
        return x**y
    three_to_the=partial(exp,3)
    print("3^2=%d" % three_to_the(2))
    cube_of=partial(exp,y=3)
    print("2^3=%d" % cube_of(2))

    #map
    xs=[1,2,3]
    cube_xs=map(cube_of,xs)
    print("Cube of xs: %s" % list(cube_xs))
    list_cuber=partial(map,cube_of)
    cube_xs=list_cuber(xs)
    print("Cube of xs: %s" % list(cube_xs))

    #filter
    def is_odd(x):
        return x%2==1
    odd_xs=filter(is_odd,xs)
    print("The odds in xs: %s" % list(odd_xs))
    list_odder=partial(filter,is_odd)
    odd_xs=list_odder(xs)
    print("The odds in xs: %s" % list(odd_xs))

    #reduce
    def multi(x,y):
        return x*y
    xs_product=reduce(multi,xs)
    print("The product of xs: %s" % xs_product)
    list_multiplier=partial(reduce,multi)
    xs_product=list_multiplier(xs)
    print("The product of xs: %s" % xs_product)

@hw1.test
def enumerating():
    text=["Foundation","Software","Science"]
    for _,i in enumerate(text):
        print(i)

@hw1.test
def zip_unpack():
    a=[1,2,3]
    b=['a','b','c']
    zip_list=list(zip(a,b))
    print("zipped list: %s" % zip_list)
    numbers,letters=zip(*zip_list)
    print("numbers: %s" % list(numbers))
    print("letters: %s" % list(letters))

@hw1.test
def arg_kwarg():
    def arg_test(*args,**kwargs):
        print("unnamed arguments: ",args)
        print("keyword arguments: ",kwargs)
    arg_test(1,2,key1="key1",key2="key2")

    def re_arg_test(x,y,z):
        return x*y*z
    x_y_list=[1,2]
    z_dict={"z":3}
    print(re_arg_test(*x_y_list,**z_dict))


if __name__=="__main__":
    hw1.report()

