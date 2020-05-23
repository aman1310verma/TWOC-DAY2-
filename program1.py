number=int(input())
# even or odd
if number % 2==0:
    print("{} in even number".format(number))
else:
    print("{} is odd number.".format(number))

#prime no.
count=0
for i in range(1,number//2):
    if number%i==0:
        count+=1
if count == 1:
    print("{} is prime number".format(number))
    
#armstrong Calculation

length=len(number)
copy=number
tot=0
for i in range(length):
    n = copy%10
    tot+= pow(n,length)
    copy=copy//10
    
print("{} in an armstrong number",.format(number))


    