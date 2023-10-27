array2D1 = eval(input())
array2D2 = eval(input())
res = "not equal"
if len(array2D1)==len(array2D1):
    res = "equal"
    for i  in range(len(array2D1)):
        if len(array2D1[i]) == len(array2D2[i]):
            j = 0
            while res != "not equal" and j < len(array2D1[i]):
                if array2D1[i][j]==array2D2[i][j]:
                    res = "equal"
                else:
                    res = "not equal"
                j+=1
        else:
            res = "unequal"
print(res)