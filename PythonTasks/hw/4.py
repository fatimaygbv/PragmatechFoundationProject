# Listin elementlərini azalan sıra ilə sıralayaraq ekrana çap edin

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def sorting(lst):
    lst.sort(reverse=True)  
    print(lst)  
sorting(myList)