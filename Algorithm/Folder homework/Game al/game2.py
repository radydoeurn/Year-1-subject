def index(arr):
    res=0
    for i in range(len(arr)):
        if arr[i]=="*":
            res=i
    return res
def moveright(arr):
    position=index(arr)
    arr[position]="0"
    arr[position]="*"
    return arr
def moveleft(arr):
    position=index(arr)
    arr[position]="0"
    arr[position-1]="*"
    return arr
arr=['0','*','0','0','0']
move=input()
for each in move:
    if each.upper()=="R":
        arr=moveright(arr)
    elif each.upper()=="L":
        arr=moveleft(arr)
print(arr)


# grid=[0,"*",0,0,0]
# def getPositonCaptain(grid):
#     for i in range(len(grid)):
#         if str(grid[i])=="*":
#             return i
# startGame=True
# while startGame:
#     positonCaptain=getPositonCaptain(grid)
#     moveCaptain=input("L/R:")
#     if moveCaptain=="L" and positonCaptain>0:
#         grid[positonCaptain]=0
#         grid[positonCaptain-1]=="*"
#     elif moveCaptain=="R" and positonCaptain<len(grid)-1:
#         grid[positonCaptain]=0
#         grid[positonCaptain+1]="*"
#     print(grid)
#     term=input("Do you want to stop? Y/N")
#     if term=="Y":
#         startGame=False