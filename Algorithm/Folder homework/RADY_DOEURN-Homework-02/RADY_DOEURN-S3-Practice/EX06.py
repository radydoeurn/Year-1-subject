array=eval(input())
result=[]
for i in range(len(array)):
    store=""
    for j in range(len(array[i])):
        store+=array[i][j].lower()
    result.append(store)
print(result)