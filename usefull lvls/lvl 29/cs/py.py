def even_or_odd(number):
    if number%2==0:
        return"Even"
    else:
        return"Odd"   #1


def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum    #2
    


def repeat_str(repeat, string):
    return string * repeat      #3




def greet():
    return "hello world!" #4




def double_integer(i):
    return i * 2     #5
