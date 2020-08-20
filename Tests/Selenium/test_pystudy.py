import functools

import pytest
from operator import itemgetter


@pytest.mark.skip(reason="dont need this")
def test_check():
    ll1 =[11,22,33,44]
    ll2= ["a","b","c","d"]
    ll3=["apple","cat","dog","meow"]
    ll4 = [1,2,3,4]
    print({c:p for p in ll1 for c in ll4 })
    ll5 = [x for x in ll2 if x != "a"]
    print(ll5)
    print(*ll5)
    dict = {c:p  for c in ll4 for p in ll1 }
    print(type(dict))
    print(dict)
    print(*dict)
    #zz =

@pytest.mark.skip(reason="dont need this")
def test_dictionaryTests():
    ll=[]

    for x in range(3):
        dict1 = {}
        dict1["item"] = "item" + str(x)
        dict1["price"] = x * 2
        ll.append(dict1)

    print(sorted(ll,key=itemgetter("price"),reverse=True))
    dd = {
        "A":{'val1':12,'val2':14,'val3':15},
        "B":{'val1':22,'val2':24,'val3':25}
         }
    for x in dd.values() :
        print(x)
    for x in dd.items():
        print(x)
        dict()
@pytest.mark.skip(reason="dont need this")
def test_unpackingoperators():
    mylist = [11,22,33,44,55,66,77]
    a,*b,c =mylist
    print(a)
    print(b)
    print(c)

def test_tuple():
    tp =  (1, "Jeff", "Computer", 75.50, True)
    print(tp)
    ll = [1, "Jeff", "Computer", 75.50, True]
    print(ll,id(ll))
    ll[0]=22
    print(ll, id(ll))
    ll = [11, "Jeff1", "Computer", 75.50, True,True]
    print(ll,id(ll))

    xx=[]
    a ="Debapriyo"
    for x in a:
        xx.append(x)
    print((xx))

    ss={}
    ss={"a",2,True,False,(22,33)}
    print(ss)















#*****DECORATOR ********************************************
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(ele):
        func(ele)
        print("with whisky")
        return 2
    return wrapper

@my_decorator
def say_cheese(element):
    print("say",element)


#say_cheese = my_decorator(say_cheese)
x=say_cheese("ghantaa")
print(x)
print(say_cheese)
print(say_cheese.__name__)
help(say_cheese)