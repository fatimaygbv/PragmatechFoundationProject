# Listin içində cüt yerdə duran elementləri ekrana çap edin

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def showEvenData():
    s=""
    for i in range(0,len(myList),2):
        s+=str(myList[i])+" "
    print(s)
showEvenData()    