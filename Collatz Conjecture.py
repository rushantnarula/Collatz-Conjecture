count=0
n=int(input("Enter the no. : "))
while n>1:
    if n%2==0:
        n=n/2
        count+=1
    else:
        n=n*3+1
        count+=1
print("Total number of steps : ", count)
