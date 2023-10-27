# text="How are you?"
# word=""
# for i in range(len(text)):
#     if text[i]!=" ":
#         word+=text[i]
#     else:
#         print(word)
#         word=""
# print(word)


text="How are you?"
word=""
array=[]
for i in range(len(text)):
    if text[i]!=" ":
        word+=text[i]
    else:
        print(word)
        word=""
    array.append(word)
print(array)