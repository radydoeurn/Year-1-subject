# arr = ["banana","apple","mango", "Coconut"]
# result=[]
# for i in range(len(arr)):
#     count=0
#     for j in range(len(arr[i])):
#         count += 1
#     result.append(count)
# print(result)


# arr = ["banana","apple","mango", "Coconut"]
# result=[]
# for i in range(len(arr)):
#     count=0
#     for j in range(len(arr[i])):
#         if arr[i][j]=="a" or arr[i][j]=="A":
#             count+=1
#     result.append(count)
# print(result)


# arr = ["banana","apple","mango", "Coconut"]
# result=[]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i]=="banana":
#             arr.append(arr[i])
#             arr.pop(i)
# print(arr)


arr = ["banana","apple","mango", "Coconut"]
result=[]
for i in range(len(arr)):
    for i in range(len(arr[i])):
        result=arr[:-1]
print(result)