def numberOfUppercase(string):
    result=0
    for i in range(len(string)):
        if string[i]==string[i] .upper():
            result+=1
    return result
string=input()
print(numberOfUppercase(string))