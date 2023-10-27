text = ["banana","apple","mengo"]
array = []
for i in range(len(text)):
    result = []
    for j in range(len(text[i])):
        result.append(text[i][j].upper())
    array.append(result)
print(array)