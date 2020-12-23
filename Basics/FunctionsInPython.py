def Hello():
    print("Hello, Welcome")

Hello()
Hello()

def Display(name, age):
    print('Hello {} you are {} years old.'.format(name,age))

Display('Jax',33)

#Default value
def Display_Deafult(name="Spark", age=0):
    print('Hello {} you are {} years old.'.format(name,age))

Display_Deafult('bel')

#using return
def MyFun():
    return "My I am superb"

callme = MyFun()
print(callme)

"""def tripleprint(data):
    print(data+data+data)
"""
def tripleprint(word):
    print(word*3)

tripleprint('hello')
