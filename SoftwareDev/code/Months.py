month = input("Input the name of the month:")
days = 0 #days set to 0 by default

if(month == "February"):
    days = "28 or 29"
elif(month == "April" and "June" and "September" and "November"):
    days = 30
elif(month == "January" and "March" and "May" and "July" and "August" and "October" and "December"):
    days = 31
    
print("No. of days:", days)