# Test 1
text1 = "Hello PNC"
result = ""
for i in range(len(text1)):
    result += text1[(len(text1)-1) - i]
print(result)

# Test 2
text2 = "Welcome 2021"
result = ""
for i in range(len(text2)):
    result += text2[(len(text2) - 1)- i]
print(result)

# function
def reversString(string):
    result=""
    for i in range(len(string)):
        result+=string[(len(string)-1)-i]
    return result

string=input("..")
print(reversString(string))