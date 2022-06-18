import math


def addition(num1,num2):
    return num1 + num2


def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2



#fixme
def division(num1,num2):
    if not num2:
        raise ValueError('Division by zero')
    return float(num1) / num2

def factorial(num1):
    if num1 < 0:
        raise ValueError('Negative factorial')
    if num1 == 0:
        return 0    
    if num1 % 1 != 0.0:
        raise ValueError('Floating number input')
    i = 1
    result = 1
    while i <= num1:
        result *= i
        i+=1
    return result

def power(num1,num2):
    return num1 ** num2

    # result = 1
    # if num2 > 0:
    #     i = 0 
    #     while i < num2:
    #         result*=num1
    #         i+=1
    # if num2 < 0:
    #     i = 0 
    #     while i > num2:
    #         result*=num1
    #         i-=1
    #     result = 1/result
    # return result

def root(num1,num2):
    if num1 < 0 and num2%2 == 1:
        num1 = -num1
        result = num1**(1.0/num2)
        return -result

    elif num1 < 0 and num2%2 != 1:
        raise ValueError('Negative fractional')

    return num1**(1.0/num2) 
