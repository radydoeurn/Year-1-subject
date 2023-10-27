def textCheng(names):
    num = []
    for i in range(len(names)):
        result = []
        for j in range(len(names[i])):
            result.append(names[i][j].upper())
        num.append(result)
    return num
names = ["heang","him","hong"]
print(textCheng(names))