from search_customer import *
def roomRent():
    import class_cid
    myConnection = class_cid.connection #importing mysql credentials from class_cid
    while True:
        customer=searchCustomer()
        if customer:
            if myConnection:
                cursor=myConnection.cursor()
                cid = class_cid.cid0
                sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"#1Checking if The CID already exists to avoid duplication/errors
                cursor.execute(sql0, (cid,))
                data = cursor.fetchall()
                try:    #using try and except method to check if any data is present in the tables
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if cid == b:
                    print("This CID Already Exist")
                    continue
                    # 2Checking if The CID already exists to avoid duplication/errors using if/else
                else:
                    checkin = input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
                    checkout = input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
                    #printing Options for the user
                    print ("\n ##### Available Rooms For Customer #####")
                    print (" 1. Ultra Royal ----> 10000 Rs.")
                    print (" 2. Royal ----> 5000 Rs. ")
                    print (" 3. Elite ----> 3500 Rs. ")
                    print (" 4. Budget ----> 2500 USD ")
                    try:
                        roomchoice =int(input("Enter Customer's Option : "))#user choice for the above option
                        try:
                            roomno=int(input("Enter Customer Room No : "))
                            try:
                                noofdays=int(input("Enter No. Of Days : "))
                                if roomchoice==1:#if elif for roomchoice initiates for the choices given to user earlier
                                    roomquality='Ultra Royal'
                                    roomrent = noofdays * 10000
                                    print("\nUltra Royal Room Rent : ",roomrent)
                                elif roomchoice==2:
                                    roomrent = noofdays * 5000
                                    roomquality = 'Royal'
                                    print("\nRoyal Room Rent : ",roomrent)
                                elif roomchoice==3:
                                    roomrent = noofdays * 3500
                                    roomquality = 'Elite'
                                    print("\nElite Royal Room Rent : ",roomrent)
                                elif roomchoice==4:
                                    roomrent = noofdays * 2500
                                    roomquality = 'Budget'
                                    print("\nBudget Room Rent : ", roomrent)
                                else:
                                    print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                                    return
                                sql = "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"  # place holder for variables
                                values = (cid,checkin,checkout,roomquality, roomchoice, noofdays, roomno,roomrent,)
                                # storing all user inputs in a single variable
                                cursor.execute(sql, values)
                                # executing the place holder and the values
                                cursor.execute("COMMIT")
                                # commiting the statement so that all values will be stored in database
                                print("The Room Has Been Booked For : ", noofdays, "Days")
                                print("The Room Quality is : Rs. ", roomquality)
                                print("The Total Room Rent is : Rs. ", roomrent)
                                cursor.close()
                            except ValueError:
                                print("Invalid Input,Please Try Again")
                        except ValueError:
                            print("Invalid Input,Please Try Again")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                    return False
            else:
                print("\nERROR ESTABLISHING MYSQL CONNECTION !")