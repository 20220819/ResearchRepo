humanage = int(input("Input a dog's age in human years: "))
dogage = 0  #dogage set to 0 by default

if(humanage == 1):
    dogage = 10.5
elif(humanage == 2):
    dogage = 21
elif(humanage >= 2):
    dogage = (((humanage-2)*4)+21)
    
print("The dog's age in human years is: ", dogage)
