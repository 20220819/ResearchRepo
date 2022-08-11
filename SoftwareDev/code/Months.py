# month = input("Input the name of the month:")
# days = 0 #days set to 0 by default

# if(month == "February"):
#     days = "28/29"
# elif(month == "April" "June" and/or "September" and/or "November"):
#     days = 30
# elif(month == "January" and "March" and "May" and "July" and "August" and "October" and "December"):
#     days = 31
    
# print("No. of days:", days)

a = ["April", "June", "September", "November"] #30 days
b = ["January", "March", "May", "July", "August", "October", "December"] #31 days
c = ["February"] #28 or 29 days

month = input("Input name of the Month:")

for i in a:
    if i == month :
        print("No. Of Days: 30")

for i in b:
    if i == month :
        print("No. Of Days: 31")
        
for i in c:
    if i == month :
        print("No. Of Days: 28/29")      
