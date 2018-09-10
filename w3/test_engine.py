import re,traceback

class o:
    y=n=0
    @staticmethod
    def report():
        print("\n pass= %s, fail= %s, %%pass= %s%%" % (o.y,o.n,round(o.y*100/(o.y+o.n+0.0001))))

    @staticmethod
    def test(f):
      try:
         print("\n------------|%s|------------" % f.__name__)
         if f.__doc__:
             print("# "+re.sub(r'\n[ \t]*',"\n",f.__doc__))
         f()
         print("pass")
         o.y+=1
      except:
         o.n+=1
         print(traceback.format_exc())
      return f