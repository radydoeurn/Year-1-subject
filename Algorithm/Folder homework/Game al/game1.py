grid=[0,"*",0,0,0]
indexCaptain=0
for i in range(len(grid)):
    if str(grid[i])=="*":
        grid[i]=0
        indexCaptain=i
grid[indexCaptain+1]="*"
print(grid)


