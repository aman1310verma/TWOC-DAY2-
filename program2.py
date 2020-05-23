def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    
    elif n==1: 
        return 0
    
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
if __int__='__main__':
    num = int(input("Enter any number"))
    print(fibonacci(num)) 
  
