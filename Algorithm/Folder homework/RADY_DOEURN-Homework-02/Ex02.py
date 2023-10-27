def snakPosition(movements, position):
    if len(movements)<len(position):
        for i in range(len(movements)):
            position[i] = 0
            position[i+1] = 1
    else:
        position[1]=0
        position[-1]= 1
position=input()
print(position)