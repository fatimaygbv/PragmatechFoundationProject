# Listin içində təkrarlanan elementləri tapın

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def function(lst):
    repeated=[]
    for i in range(len(lst)):
        if lst.count(lst[i])==2 and lst[i] not in repeated:
            repeated.append(lst[i])
    lst=repeated
    print(lst)
function(myList)