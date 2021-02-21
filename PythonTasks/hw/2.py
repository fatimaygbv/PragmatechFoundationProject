# Listin eleməntlərini ekrana çap edin

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def showData():
    s=""
    for x in range(len(myList)):
        s+=str(myList[x])+" "
    print('My list:',s)    
showData()    