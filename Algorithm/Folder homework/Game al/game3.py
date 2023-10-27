def index(arrays):
    result =[]
    for i in range(len(arrays)):
        for value in range(len(arrays)):
            if arrays[i][value]:
                result.append(1)
                result.append(value)
    return result
def moveright(arrays):
    position = index(arrays)
    row  = position[0]
    col = position[1]
    arrays[row][col] = "0"
    arrays[row][col+1] = "*"
    return arrays
def moveleft (arrays):
    position = index(arrays)
    row = position[0]
    col = position[1]
    arrays[row][col]= "0"
    arrays[row][col-1]= "*"
arrays =[[]]
move = input()
stop = index(arrays)
for each in move:
    if each.upper()=="R":
        arrays = moveright(arrays)
    elif each.upper()=="L":
        arrays= moveleft(arrays)
print(arrays)