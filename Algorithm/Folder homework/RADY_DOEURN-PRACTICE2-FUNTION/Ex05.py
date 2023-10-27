# Test 1
number1 = 20
number2 = 100
result = number2
if number1 > number2:
    result = number1
print("Maximum is " + str(result))

# Test 2
num1 = 200
num2 = 300
result = num2
if num1 > num2:
    result = num1
print("Maximum is " + str(result))

# function
def max(num1,num2):
    result=num2
    if num1 > num2:
        result=num1
    return result

num1=int(input(".."))
num2=int(input(".."))
print(max(num1,num2))