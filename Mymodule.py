import math
def greet(name):
    print(f"Hi, {name} from userdefined module!")
def even(lst):
    even_lst = []
    for i in lst:
        if i%2==0:
            even_lst.append(i)
    return even_lst

def fact(num):
    return math.factorial(num)


