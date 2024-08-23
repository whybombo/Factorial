number = int(input("Enter the Number: "))

factorial = 1

if (number < 0):
    
    print("No negative numbers")

elif (number < 2):
    
    print("{}! = {}".format(number,factorial))

else:
            #ex. 4 to 1 and -1 is like 4 3 2 1
    for num in range(number,1,-1):
        factorial = factorial * num
        
    print("{}! = {}".format(number,factorial))
