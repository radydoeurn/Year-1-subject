def comment(grade):
    result="Bad"
    if grade>10:
        result="Good"
    return result
grade=int(input())
print(comment(grade))