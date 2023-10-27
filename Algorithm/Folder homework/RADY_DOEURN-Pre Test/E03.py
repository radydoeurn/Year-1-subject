numbers=eval(input())
total=[]
for i in range(len(numbers)):
    if numbers[i]<10:
        total+=[numbers[i]]
print(total)


