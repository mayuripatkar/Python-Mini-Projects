yr = int(input("Enter the year:"))
if (yr%4 == 0):
    if (yr%100 ==0):
        if (yr%400 == 0):
            print("Year '{}' is a leap year".format(yr))
        else:
            print("Year '{}' is not a leap year".format(yr))
    else:
        print("Year '{}' is a leap year".format(yr))
else:
    print("Year '{}' is not a leap year".format(yr))
    
