date = input("Enter a date: ")
if len(date) == 10 and date[2] == "/" and date[5] == "/" and (date[:2]+date[3:5]+date[6:]).isdigit():
    day = date[:2]
    month = date[3:5]
    year = date[6:]
    if int(month) < 1 or int(month) > 12:
        print("Invalid date!")
    else:
        if int(month) in [1,3,5,7,8,10,12] and 0 < int(day) <= 31:
            print(year,"-",month,"-",day,sep="")
        elif int(month) in [4,6,9,11] and 0 < int(day) <= 30:
            print(year,"-",month,"-",day,sep="")
        elif int(month) == 2 and 0 < int(day) <= 28:
            print(year,"-",month,"-",day,sep="")
        else:
            print("Invalid date!")
else:
    print("Invalid date!")
