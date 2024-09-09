def powerq(n):
    if(n == 0):
        return 0
    elif((n &(~(n-1)))):
        return 1 
    return 0 
    
    num = int(input("Enter a number:"))
    if(power2(num)):
        print("The number is power of 2 ")
    else:
        print("The number is not power of 2")
