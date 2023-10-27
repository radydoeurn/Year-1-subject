array=eval(input())
indexOfcolumn=int(input())
for i in range(len(array)):
    for j in range(len(array[i])):
        if indexOfcolumn==j:
            array[i][j]="*"
if indexOfcolumn>j:
    array="column error"
print(array)