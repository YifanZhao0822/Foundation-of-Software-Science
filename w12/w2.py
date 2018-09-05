import re,traceback

class hw2:
    y=n=0
    @staticmethod
    def report():
        print("\n pass= %s, fail= %s, %%pass= %s%%" % (hw2.y,hw2.n,round(hw2.y*100/(hw2.y+hw2.n+0.0001))))

    @staticmethod
    def test(f):
      try:
         print("\n------------|%s|------------" % f.__name__)
         if f.__doc__:
             print("# "+re.sub(r'\n[ \t]*',"\n",f.__doc__))
         f()
         print("pass")
         hw2.y+=1
      except:
         hw2.n+=1
         print(traceback.format_exc())
      return f

DATA1="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

def lines(s):
    "Return contents, one line at a time."
    result=[]
    ss=s.split("\n") #split the data string by \n
    for line in ss:
       result.append([line]) #each line is a entry in the returned list
    return result

def rows(src):
    """Kill bad characters. If line ends in ','
     then join to next. Skip blank lines."""
    row=[]
    mid=[]
    src.remove([""]) #delete the blank lines
    for line in range(len(src)):
        mid.append(src[line][0].split()) #split the string by space and store it to a new list
        try:
            flag=mid[line].index("#")   #find comments in the list
            for po in range(flag,len(mid[line])):
                mid[line].pop()   #delete comments
        except ValueError:       #ignore these lines if the entry doesnt have a comment
            pass

        try:
            row.append(mid[line][0].split(","))#split the entry by comma and store it to a new list
        except IndexError:  #ignore the line above if there is a null list, i.e., [] in mid
            pass

        if line>0:
            if not row[-2][-1]: #since we splitted the list by comma, the lines ending with a comma will have its last entry null
                row[-2].pop(-1)
                row[-2].extend(row[-1]) #if the last line ends with a comma, extend it with the next line
                row.pop(-1)

    return row

def cols(src):
    """ If a column name on row1 contains '?',
    then skip over that column."""

    for col in range(len(src[0])):
        try:
            if src[0][col][0]=="?": #search for question mark and delete the corresponding column
                for row in range(len(src)):
                    src[row].pop(col)
        except IndexError: #ignore the index problem after deleting
            break
    return src

def prep(src):
    """ If a column name on row1 contains '$',
    coerce strings in that column to a float."""
    for col in range(len(src[0])):
        if src[0][col][0]=="$":
            for row in range(1,len(src)):
                src[row][col]=float(src[row][col])
    return src

def ok0(s):
    for row in prep(cols(rows(lines(s)))):
        print(row)

@hw2.test
def ok1():
    ok0(DATA1)

@hw2.test
def ok2():
    ok0(DATA2)


if __name__=="__main__":
    hw2.report()