def arrayNumber(numbers):
    result=0
    for i in range(len(numbers)):
        result+=numbers[i]
    return result
num1=eval(input())
num2=eval(input())
print(sum(num1))
print(sum(num2))