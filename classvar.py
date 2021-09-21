from memory_profiler import profile
import psutil,os,gc
paraalist=[]
class BaseAClassVars():
    print("类变量，会在此模块加载中自动执行1次")
    a=[]
    for i in range(10000000):
        a.append(i)
        paraalist.append(i)

class BaseAClassInstancesVars():

    def __init__(self):
        print("类实例变量，每次实例化的时候都会执行")
        self.a=[]
        for i in range(10000000):
            self.a.append(i)
            paraalist.append(i)

class A(BaseAClassVars):
    @profile
    def __init__(self):
        self.aa=BaseAClassVars()

class AA(BaseAClassInstancesVars):
    @profile
    def __init__(self):
        self.aa=BaseAClassInstancesVars()

def main():
    for i in range(10000):
        # A()
        AA()

if __name__=="__main__":
    main()

