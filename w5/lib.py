import random

def cat(lst,sep=","):
    result=""
    for entry in lst:
        entry=str(entry)
        result+=entry
        result+=sep

    return result

def dump(lst,sep=","):
    for entry in lst:
        entry=list(entry.values())
        entry=cat(entry)
        print("%s" % entry+sep)

def another(x,lst):
    y=random.choice(range(len(lst)))
    if x==y:
        return another(x,lst)
    if lst[y]:
        return lst[y]
    return another(x,lst)

def fyi(x):
    print(x+"\n")

def ksort(c,rows):
    index={}
    result=[]
    for i in range(len(rows)):
        row=rows[i][c]
        row+=random.randint(0,100)/10000
        index[row]=i
    for key in sorted(index.keys()):
        result.append(rows[index[key]])
    return result