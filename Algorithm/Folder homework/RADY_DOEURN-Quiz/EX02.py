def containUpperCase(word):
    result=""
    for i in range(len(word)):
        if word=="" .upper():
            result="Valid"
        else:
            result="Invalid"
    return result
word=input()
print(containUpperCase(word))

