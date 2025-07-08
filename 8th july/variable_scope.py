#LEGB rule in variable scope
# 1. local 2.Enclosed 3.Global 4.Built-in(min,max)

#buil-in error
# def min():
#     pass
# a = min[10,20,30,41]
# print(a)

#enclosed global and local variable
def outer():
    x="outer x"

    def inner():
        x = "inner x"
        print(x)

    inner()
    print(x)
outer()

#non local
def outer():
    x="outer x"

    def inner():
        nonlocal x
        x = "inner x"
        print(x)

    inner()
    print(x)
outer()

#global

x = "hello world"
def outer():
    x="outer x"

    def inner():
        x = "inner x"
        print(x)

    inner()
    print(x)
outer()
print(x)