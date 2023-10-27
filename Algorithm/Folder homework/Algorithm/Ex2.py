arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
count=0
for i in range(len(arr)):
    if arr[i]=="banana" or arr[i]=="Banana":
        count+=1
print(count)


# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
# count=0
# for i  in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]=="o":
#             count+=1
# print(count)


# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
# for i in range(len(arr)):
#     if arr[i]=="banana" or arr[i]=="Banana":
#        arr[i] = "jackfruit"
# print(arr)


# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
# array=[]
# for i in range(len(arr)):
#     if arr[i].lower() not in array:
#         array.append(arr[i])
# print(array)


# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
# result=[]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]=="a" or arr[i][j]=="c":
#             result+=arr[i][j].upper()
# print(result)