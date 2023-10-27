def getArrayOfNumber3(array):
    row=0
    col=0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==3:
                row=i
                col=j
    return [row, col]
array=eval(input())
print(getArrayOfNumber3(array))