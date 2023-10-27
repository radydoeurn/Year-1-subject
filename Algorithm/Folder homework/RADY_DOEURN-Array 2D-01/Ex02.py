array = [[56, 80, 28],[35, 43, 20],[82, 43, 69]]
for i in range(len(array)):
    subjectFail = 0
    for j in range(len(array[i])):
        if array[i][j] < 50:
            subjectFail += 1
    print("Student in row number "+ str(i+1) +" fail "+ str(subjectFail) +" subject")