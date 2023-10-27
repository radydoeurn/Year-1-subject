# text=input()
# result=0
# count=0
# for i in range(len(text)):
#     count+=1
#     if i>1:
#         if text[i]=="c" and text[i-1]=="b" and text[i-2]=="a":
#             result="Ok"
#         else:
#             result="wrong"
# print(result)


# text = input()
# result = ""
# isNumber = True
# for i in range(len(text)):
#     if i > 0:
#         if text[i] > text[i-1] and isNumber == True:
#             result = "SORTED"
#         elif text[i]==text[i-1]:
#             result="SORTED"
#         else:
#             result = "NOT SORTED"
#             isNumber= False
# print(result)


# text=input()
# result="SORTED"
# for i in range(len(text)-1):
#     if text[i+1]<text[i]:
#         result="NOT SORTED"
# print(result)


# text = input()
# is_wrong_display =""
# result =''
# for i in range(len(text)):
#     if text[i] =='x':
#         result = 'OK'
#     elif i+1<len(text) and text[i] == '[' and text[i+1] == 'y':
#         result ='OK'
#     elif i+1<len(text) and text[i] == 'y' and (text[i+1] ==']' or text[i+1] =='y') and i !=0 and text[i-1] !='x':
#         result ='OK'
#     elif text[i] ==']' and text[i-1] =='y':
#         result ='OK'
#     else:
#         is_wrong_display = True
# if is_wrong_display == True:
#     print("WRONG")
# else:
#     print(result)


# 

# def dayOff():
#     print("I love you")
# dayOff()

# def dayOff(rady,Iwanttomarryu):
#     print("Hello "+rady+" and "+ str(Iwanttomarryu))
# dayOff("I love you baby", 56)
# dayOff("I love you boy", 65)
# dayOff("I love you girl", 76)

# def get(name,age):
#     print("my name is "+name+" and my ageis"+str(age))
# get("Yon",12)
# get("Yen",11)

# def getFullName(name,othername):
#     return "My name is"+name+ othername
# print(getFullName(" yon"," yen"))
# print(getFullName(" rady"," y"))

# def sumNumber(number1,number2):
#     return (number1+number2)
# print(sumNumber(5,12))
# print(sumNumber(3,17))

# def countNumberOfX(text):
#     count=0
#     for i in range(len(text)):
#         if text[i]=="X":
#             count+=1
#     return count
# print(countNumberOfX("XXAACCXJXXXXXXXX"))
# inputword=input("Enter a word:")
# print(countNumberOfX(inputword))

# def goOd(name):
#     print("Good morning"+name+" !")
#     print("Good night sweet dream!")
#     print("Good bye!")
# goOd(" rady")
# goOd(" KD")

# def disPlayname():
#     name="hin"
#     print(name)
# print="rady"
# print="tit"

# def removeMinuses(text):
#     newWord=""
#     for i in range(len(text)):
#         if text[i] != "-":
#             newWord= newWord+text[i]
#     return newWord
# isContinue = True
# while isContinue==True:
#     text= input()
#     print(removeMinuses(text))
#     word = input("Enter new word:")
#     if word =="N":
#         isContinue=False

# def sumNumber(num1,num2):
#     result=0
#     if num1!="" and num2


# def numberOfUpperCases(text):
#     for i in range(len(text)):
#         if text[i].isupper():
#             sum +=1
#         return sum
# text = input("Enter :")
# print(numberOfUpperCases(text))


# def sumNumber(number1,number2):
#     result=0
#     if number1!="" and number2!="":
#         result=number1+number2
#         return result
# number1=int(input())
# number2=int(input())
# print(sumNumber(number1,number2))


# def removeMinuses(text):
#     newWord=""
#     for i in range(len(text)):
#         if text[i] != "-":
#             newWord= newWord+text[i]
#     return newWord
# isContinue = True
# while isContinue==True:
#     text= input()
#     print(removeMinuses(text))
#     word = input("Enter new word:")
#     if word =="N":
#         isContinue=False
# def sumFromTo(start,end):
#     total = 0
#     for i in range(start,end + 1,1):
#         total += i
#     return total

# start = int(input("Inter your start number: "))
# end = int(input("Inter your end number: "))
# print(sumFromTo(start,end))

def sumNumber():
    value=int(input("..."))
    result=0
    for i in range(value):
        number=int(input())
        result+=number
    return result
print(sumNumber())