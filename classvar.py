paraalist=[]
class BaseA():
    # print("类变量")
    # a=[]
    # for i in range(10000000):
    #     a.append(i)
    #     paraalist.append(i)
    def __init__(self):
        print("类实例变量")
        self.a=[]

        for i in range(10000000):

            self.a.append(i)
            paraalist.append(i)

class A(BaseA):

    def __init__(self):
        self.aa=BaseA()

for i in range(10000000):

    A()