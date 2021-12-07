# def add(val1, val2):
#     return val1 + val2

def add(*args):
    return args[0] + args[1] + args[2]

def sub(val1, val2):
    return val1 - val2

sum = add(1, 2, 3)
print (f"The sum is {sum}")

# diff = sub(1, 2)
# #print ("The difference is " + str(diff))
# print (f"The difference is {diff}")

def sub(**kwargs):
    return kwargs['val1'] - kwargs['val2'] - kwargs['val3']

diff = sub(val1=1, val2=2, val3=3)
print (f"Difference is: {diff}")