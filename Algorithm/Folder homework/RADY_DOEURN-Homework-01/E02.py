def arrayNumber(number):
    result=0
    for i in range(number):
        result+=number[i]
    return result
number1=eval(input())
number2=eval(input())
print(sum(number1))
print(sum(number2))