year = int(input("Enter the year which you want to check ,its leap year or not: "))
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print ("Its a leap year")
        else:
            print ("Its not a leap year") 
    else:
        print ("Its a leap year")   
else:
    print ("Its not a leap year")