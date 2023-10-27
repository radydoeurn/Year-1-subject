# text=input()
# result=0
# i=0
# while (text[i]) !="7":
#         result +=int(text[i])
#         i+=1
# print(result)

# result=0
# text=input()
# isfoundSeven="true"
# i=0
# for i in range (len(text)):
#     if text[i]=="7":
#             isfoundSeven!=True   
#     elif isfoundSeven== True:
#           result+=int(text[i])
# print(result)


# number=int(input("your number"))
# res=number
# for i in range(number):
#     res=number-i
#     print(res , end=" ")


# text=input("write your text")
# for i in range(len(text)):
#     if text=="Rady":
#         print("Yes")
#     else:
#         print("No")


# water=int(input("quantity of water"))
# if water>=3:
#     print("Good")
# else:
#     print("No")


# text=input()
# result=0
# for i in range(len(text)):
#     if text[i]=="A" or text[i]=="a":
#         result+=1
# print(len(text))
# print(result)


# text=input()
# sum=0
# for i in range(len(text)):
#     sum=sum+int(text[i])
# print(sum)
# print(sum/int(text[0]))


# text = input()
# result = ""
# Isnumber = True
# for i in range(len(text)):
#     if i > 0:
#         if text[i] > text[i-1] and Isnumber == True:
#             result = "SORTED"
#         elif text[i]==text[i-1]:
#             result="SORTED"
#         else:
#             result = "NOT SORTED"
#             Isnumber= False
# print(result)

# text="22 33 44"
# number=0
# index=0
# while number!=68 and index<3:
#     number=int(input())
#     if number==68:
#         message="you won"
#     else:
#         print("Try again")
#     index+=1
# print(message)

# n1 = int(input())
# n2 = int(input())
# sum = -1
# if n2 > n1:
#     sum = n1 + n2
# print(sum)

# n=input()
# result=False
# for i in range(len(n)):
#     if n[i]=="A" or n[i]=="a":
#         result=True
# print(result)

# text = input()
# result = -1
# for index in range(len(text)-1):
#     letter = text[index]
#     if letter == "K" and text[index + 1] == "K":
#         result = index
# print(result)

# text=""
# result=""
# while text !="end":
#     text=input()
#     if text!="end" and int(text)%2==0:
#         result+=text+":"
# print(result[:-1])


# text=input()
# sum=0
# if len (text)==5 and text[2]==";":
#     sum+=int(text[:2])+int(text[3:])
#     print(sum)
# else:
#     print("Wrong Format")


text=input()
name=input()
for i in range(5):
    print(text,end=" ")
    for j in range(5-i):
        print(name,end="")
    print()
   
       



