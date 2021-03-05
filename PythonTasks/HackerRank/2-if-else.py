# Python If-Else

n=int(input('Enter number: ').strip())
if n in range(1,101):
    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    if n in range(2,6) and n%2==0 :
        print('Not Weird')
    # If n is even and in the inclusive range of 6 to 20, print Weird            
    elif n in range(6,21) and n%2==0:
        print('Weird')
    # If n is even and greater than 20, print Not Weird
    elif n%2==0 and n>20:
        print('Not Weird')
    # If n is odd, print Weird
    elif n%2==1:
        print('Weird')