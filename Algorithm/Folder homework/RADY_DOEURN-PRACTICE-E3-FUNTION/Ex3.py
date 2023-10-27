def sumfromto(numbers):
    total=0
    if numbers[0]<numbers[1]:
        for i in range(numbers[0],numbers[1],1):
            total+=i
            return total
numbers=eval(input())
print(sumfromto(numbers))