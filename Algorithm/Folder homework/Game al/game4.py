# def index(arr):
#     res = []
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]=="*":
#                 res.append(i)
#                 res.append(j)
#     return res
# def moveRight(arr):
#     position = index(arr) 
#     row = position[0]
#     col = position [1]
#     arr[row][col] = '0'
#     arr[row][col+1]= '*'
#     return arr
# def moveLeft(arr):
#     position = index(arr)
#     row = position[0]
#     col = position [1]
#     arr[row][col] = '0'
#     arr[row][col-1]= '*'
#     return arr
# def moveUp(arr):
#     position = index(arr)
#     row = position[0]
#     col = position [1]
#     arr[row][col] = '0'
#     arr[row-1][col]= '*'
#     return arr
# def moveDown(arr):
#     position = index(arr)
#     row = position[0]
#     col = position [1]
#     arr[row][col] = '0'
#     arr[row+1][col]= '*'
#     return arr

# arr = [
#     ['0','*', '0','0','0'],
#     ['0','0', '0','0','0'],
#     ['0','0', '0','0','0'],
#     ['0','0', '0','0','0'],
#     ['0','0', '0','0','0']
#        ]
# stop = True
# while stop:
#     move = input()
#     if len(move)==1:
#         if move.upper()=="R":
#             arr= moveRight(arr)   
#         elif move.upper()=="L":
#             arr= moveLeft(arr)  
#         elif move.upper()=="U":
#             arr= moveUp(arr)  
#         elif move.upper()=="D":
#             arr= moveDown(arr)
#         print(arr)
#     elif move == "stop":
#         stop =  False
#         print("Game ends")
#     else:
#         stop =  False
#         print("Error comand")



grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, "*", 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

grid[1]
def getPositionCaptian(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if str(grid[row][col]) == "*":
                return [row, col]

startGame = True
print(grid)
while startGame:
    positionCaptain = getPositionCaptian(grid)
    row = positionCaptain[0]
    col = positionCaptain[1]
    moveCaptain = input("L/R/D/U: ")
    if moveCaptain == "L" and col > 0:
        grid[row][col] = 0
        grid[row][col - 1] = "*"
    elif moveCaptain == "R" and col < len(grid[0])-1:
        grid[row][col] = 0
        grid[row][col + 1] = "*"
    elif moveCaptain == "U" and row > 0:
        grid[row][col] = 0
        grid[row - 1][col] = "*"
    elif moveCaptain == "D" and row  < len(grid) -1:
        grid[row][col] = 0
        grid[row + 1][col] = "*"
    
    
    print(grid)
    term = input("do you want to stop? Y/N")
    if term == "Y":
        startGame = False