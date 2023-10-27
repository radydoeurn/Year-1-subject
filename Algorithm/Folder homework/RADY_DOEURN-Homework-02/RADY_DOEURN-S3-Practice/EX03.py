position = [0, 1, 0, 0, 0, 0]
text = input("We need one character to move the position of snake to right (R) :")

sumOfR = 0
sumOfL = 0
for i in range(len(text)):
    if text[i].upper() == "R":
        sumOfR += 1
    elif text[i].upper() == "L":
        sumOfL += 1

if sumOfR > sumOfL :
    times = sumOfR -sumOfL
    for i in range(len(position)):
        if position[i] == 1 :
            position[i] = 0
            if times < 5 :
                position[times + 1] = 1
            else:
                position[len(position)-1] = 1
elif sumOfL > sumOfR:
    times = sumOfL-sumOfR
    for i in range(len(position)):
        if position[i] == 1 :
            position[i] = 0
            if times < 2 :
                position[i - 1] = 1
            else:
                position[0] = 1
print(position)