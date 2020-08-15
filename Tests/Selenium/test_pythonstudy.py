from itertools import cycle
from time import sleep


def test_first():
    print("1st testcase")
    """
    inp = input("enter password")
    print("inp is of type"+str(type(inp)))
    assert int(inp) == 1234
    """
#print-------------------------------------------
def test_printScenarios():
    print("2nd test case","asdsa"+"gsfd" "fgjfgj""dssd")
    print("new stuff learnt 'today'")
    #escape characters--------------------
    print("I said its \"great stuff\"")
    print("C:\\User\\debo") #escape characters
    print(r'C:\Users\jdoe') #turning off character escaping
    #separators --------------------
    print("string",2,"age",43)
    print("string", 2, "age", 43,sep=None)#takes default 'space'
    print("string","name","sex")
    print("string", "name", "sex",sep='')
    print("string", "name", "sex", sep='->')
    print("string", "name", "sex", sep='\n')
    print("string", "name", "sex", sep=',')
    #end with--------------------
    # ------
    print("another one", end='/')
    print("another starts")
    print("one", end='') #disables default \n
    print("starts")
    print('Mercury', 'Venus', 'Earth', sep='>', end=', ')
    print('Mars', 'Jupiter', 'Saturn',sep='>')

    """
    #cycle  animation
    for frame in cycle(r'-\|/-\|/'):
        print('\r', frame, sep='', end='', flush=True) #flushes the buffer
        sleep(0.2)
    """
    """
    #progress bar
    def progress(percent=0, width=30):
        left = width * percent // 100
        right = width - left
        print('\r[', '#' * left, ' ' * right, ']',f' {percent:.0f}%',sep='', end='', flush=True)

    for i in range(101):
        progress(i)
        sleep(0.1)
    """
    #formatted output
    val ="ford"
    quantity = 5
    print(f"i want to buy {quantity} {val}")
#String ---------------------------------------
def test_string():
    print("type :",type("hasgd"))
    val="abcdef"
    print(val)
    print(val[0]) #Returns the character at the given index
    print(""" this
    is a 
    multiple line output""")
    print("["+"#"*10+"]") #Concatenates multiple copies of the same string
    print(val[0:2]) #	Fetches the characters in the range
    print("old C style %s "%val)
    name = "Bill"
    age =25
    mystr = "My name is {} nd age is {}"
    print(mystr.format(name,age))


