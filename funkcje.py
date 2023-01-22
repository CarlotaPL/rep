def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def fizzbuzz(i):
    if isinstance(i, (int,float)) and i>0:
        i = round(i)
        if i%3 ==0 and i%5 == 0:
            return "FizzBuzz"
        elif i%3== 0:
            return "Fizz"
        elif i%5 == 0:
            return "Buzz"
        else:
            return i
    else:
        return "Number out of range"

