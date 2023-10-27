array2d=[9,9,8,8,7]
array=[]
for i in range(len(array2d)):
    a=array2d[i]
    count=0
    for i in range(len(array2d)):
        if a==array2d[i]:
            count+=1
        if count>1 and a not in array:
            array.append(a)
print(array)