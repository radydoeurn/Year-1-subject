# myText=input()
# theTotalScoreIs=0
# for i in range(len(myText)):
#     if myText[i]=="A":
#         theTotalScoreIs+=5
#     elif myText[i]=="a":
#         theTotalScoreIs+=10
#     else:
#         theTotalScoreIs+=1
# print(theTotalScoreIs)

# theWord=input()
# countA=0
# countB=0
# for i in range(len(theWord)):
#     if theWord[i]=="A":
#         countA+=1
#     elif theWord[i]=="B":
#         countB+=1
# if countB<countA:
#     print("WELL DONE")
# else:
#     print("LOST")


text=input()
countA=0
countdollar=0
score=0
for i in range(len(text)):
    if text[i]=="A":
        countA+=1
    elif text[i]=="$":
        countdollar+=1
if countA==1:
    score+=30
if countdollar==2:
    score+=20
if countA<1 and countdollar==1:
    score+=10
print(score)
