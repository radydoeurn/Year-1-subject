text=input(" ")
for i in range(len(text)):
    sum=len(text)+i
    i+=i
    print(sum)
    if text!=10 and text!=12 and sum==20:
        print("Won")
    elif text==10 and text==12 and sum==20:
        print("Lost")