def sumNumber():
    value=int(input("..."))
    result=0
    for i in range(value):
        number=int(input())
        result+=number
    return result
print(sumNumber())
