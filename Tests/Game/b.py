class Great:

    val1 = 1
    val4=10
    ll=[]
    print("here outside")
    def __init__(self, value):
        self.val1=value
        self.val2= 0
        print("constructor",self)

    def __init__(self,value,value2):
        print("2nd constructor")

    def fun(self):
        val3 = self.val1+2
        print("##",val3)
    def get(self):
        print(self.val4,self)

    @classmethod
    def classmethod(cls):
        print('class method called', cls)

    @staticmethod
    def staticmethod():
        print('static method called')


class Sub(Great):
    def __init__(self):
        pass
    def fun1(self):
        self.val1 = 22
obj = Great(1,2)
obj.classmethod()
obj.staticmethod()
print(obj.__dir__())
"""
obj.val4=22
obj.ll.append(1)
print(obj.val4,obj.ll)
print(obj.__dict__)
print(obj2.val4,obj.ll)
print(obj2.__dict__)
print(Great.val4)
print(Great.__dict__)
"""






