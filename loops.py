#print 7 to 19

i = 7
while(i<=19): # this compares is i less than or equal to 19 and the while repeats it until the contion is true
    i += 1    #this add one to i
    print(i)  #this print i to the screen
    
j = 10
while (j <= 20):
    j += 2
    print(j)
    
def evens():
    k = int(input("please input first number"))
    m = int(input("please input second number"))
    while(k<m):
        if(k % 2 == 0):
            k += 2
            print(k)
    
        else:
            k += 1
            print(k)
        
    
evens()


def reverse_evens():
    k = int(input("please input first number"))
    m = int(input("please input second number"))
    while(m>k):
        if(m % 2 == 0):
            m -=2
            print(m)
        else:
            m -=1
            print(m)
    
    
reverse_evens()