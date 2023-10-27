# numbers=eval(input())
# total=[]
# for i in range(len(numbers)):
#     if numbers[i]<10:
#         total+=[numbers[i]]
# print(total)

numbers=eval(input())
arrayOfOneDigitNumber=[]
for i in range(len(numbers)):
    if str(numbers[i])==1:
        numbers.append(arrayOfOneDigitNumber)
print(numbers)
