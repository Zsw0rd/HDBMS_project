def altdel_rec():
    import class_cid
    myConnection =class_cid.connection
    cursor = myConnection.cursor()
    print("""
        1--->Alter/Edit Record
        2--->Delete Record
        3--->Exit""")
    try:
        a=int(input("Enter Yourr Choice"))
        if a==1:
            print("""
                    1--->Edit a Record in Customer Details
                    2--->Edit a Record in Room Details
                    3--->Edit a Record in Restaurent Bill Details
                    4--->Edit a Record in Gaming Details
                    5--->Edit a Record in Fashion Details
                    6--->Exit
                    """)
            try:
                b=int(input("Enter Your Choice"))
                if b == 1:
                    print("You Have selected to Edit a Record In Customer Table Details")
                    print("""
                        1--->Edit a Record in Customer ID Details
                        2--->Edit a Record in Name Details
                        3--->Edit a Record in Address
                        4--->Edit a Record in Age Details
                        5--->Edit a Record in Country Details
                        6--->Edit a Record in PhoneNO Details
                        7--->Edit a Record in PhoneNO Details
                                        """)
                    try:
                        c=int(input("Enter Your Choice:"))
                        if c==1:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter New Customer ID:")
                                sql="UPDATE C_DETAILS SET CID=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==2:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated Name:")
                                sql="UPDATE C_DETAILS SET C_NAME=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==3:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated Address:")
                                sql="UPDATE C_DETAILS SET C_ADDRESS=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==4:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated AGE:")
                                sql="UPDATE C_DETAILS SET C_AGE=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==5:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated Country:")
                                sql="UPDATE C_DETAILS SET C_COUNTRY=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==6:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated phoneno:")
                                sql="UPDATE C_DETAILS SET P_NO=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==7:
                            cid=input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2=input("Enter Updated EMAIL:")
                                sql="UPDATE C_DETAILS SET C_EMAIL=%s WHERE CID=%s"
                                cursor.execute(sql,(cid2,cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 2:
                    print("You Have selected to Edit a Record In Room Rent Table Details")
                    print("""
                            1--->Edit a Record in Customer ID Details
                            2--->Edit a Record in Room Quality,Room Rent,Room Choice,NO OF DAYS Details
                            3--->Edit a Record in Room NO. Details
                            4--->Edit a Record in CHECKIN date
                            5--->Edit a Record in CHECKOUT date
                                                            """)
                    try:
                        c = int(input("Enter Your Choice:"))
                        if c == 1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter New Customer ID:")
                                sql = "UPDATE ROOM_RENT SET CID=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 2:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                print("""Edit Room Choice To Update Room quality,Room Rent ,No of Days and Total Bill""")
                                print (" 1. Ultra Royal ----> 10000 Rs.")
                                print (" 2. Royal ----> 5000 Rs. ")
                                print (" 3. Elite ----> 3500 Rs. ")
                                print (" 4. Budget ----> 2500 USD ")
                                try:
                                    cid2 = int(input("Enter Updated Choice:"))
                                    if cid2 == 1:
                                        try:
                                            noofdays=int(input("\nEnter updated No of days or enter it as the same"))
                                            roomquality = 'Ultra Royal'
                                            roomrent = noofdays * 10000
                                            sql = "UPDATE ROOM_RENT SET ROOM_CHOICE=%s,ROOM_QUALITY=%s,NO_OF_DAYS=%s,ROOMRENT=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,roomquality,noofdays,roomrent,cid,))
                                            cursor.execute("COMMIT")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 == 2:
                                        try:
                                            noofdays=int(input("\nEnter updated No of days or enter it as the same"))
                                            roomrent = noofdays * 5000
                                            roomquality = 'Royal'
                                            sql = "UPDATE ROOM_RENT SET ROOM_CHOICE=%s,ROOM_QUALITY=%s,NO_OF_DAYS=%s,ROOMRENT=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,roomquality,noofdays,roomrent,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 == 3:
                                        try:
                                            noofdays = int(input("\nEnter updated No of days or enter it as the same"))
                                            roomrent = noofdays * 5000
                                            roomquality = 'Royal'
                                            sql = "UPDATE ROOM_RENT SET ROOM_CHOICE=%s,ROOM_QUALITY=%s,NO_OF_DAYS=%s,ROOMRENT=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, roomquality, noofdays, roomrent, cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 == 4:
                                        try:
                                            noofdays=int(input("\nEnter updated No of days or enter it as the same"))
                                            roomrent = noofdays * 3500
                                            roomquality = 'Elite'
                                            sql = "UPDATE ROOM_RENT SET ROOM_CHOICE=%s,ROOM_QUALITY=%s,NO_OF_DAYS=%s,ROOMRENT=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,roomquality,noofdays,roomrent,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif c == 5:
                                        cid = input("Enter Customer ID:")
                                        sql0 = "SELECT CID FROM BOOKING_RECORD WHERE CID=%s"
                                        cursor.execute(sql0, (cid,))
                                        data = cursor.fetchall()
                                        try:
                                            b = data[0][0]
                                        except IndexError:
                                            b = ['null']
                                        if cid == b:
                                            cid2 = input("Enter Updated CHECKOUT Date:")
                                            sql = "UPDATE BOOKING_RECORD SET CHECK_OUT=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        else:
                                            print("Record You are Trying to Modify doesnt exist")
                                    else:
                                        print("Invalid Input")
                                except ValueError:
                                    print("Invalid Input,Please Try Again")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 3:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid==b:
                                cid2 = input("Enter Updated ROOMNO.:")
                                sql = "UPDATE ROOM_RENT SET ROOMNO=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 4:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM BOOKING_RECORD WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter Updated CHECKIN DATE:")
                                sql = "UPDATE BOOKING_RECORD SET CHECK_IN=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 3:
                    print("You Have selected to Edit a Record In Restaurent Table Details")
                    print("""
                        1--->Edit a Record in Customer ID Details
                        2--->Edit a Record in Order no. Details
                        3--->Edit a Record in Cuisine Choice,Cuisine,Quantity,Bill  Details
                        4--->Edit a Record in  Details
                        5--->Edit a Record in  Details
                        6--->Edit a Record in Details
                                                        """)
                    try:
                        c = int(input("Enter Your Choice:"))
                        if c == 1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM Restaurent WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter New Customer ID:")
                                sql = "UPDATE RESTAURENT SET CID=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 2:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM Restaurent WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter Updated OrderNo:")
                                sql = "UPDATE RESTAURENT SET ORDER_NO=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 3:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM Restaurent WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                print("""Edit Cusine Choice To Update Cuisine,Quantity And Bill""")
                                print("1. Vegetarian Combo -----> 300 Rs.")
                                print("2. Non-Vegetarian Combo -----> 500 Rs.")
                                print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
                                print(" To Edit Beverages ")
                                print("""
                                        4.Coffee-----> 200 Rs.
                                        5.Tea-----> 150 Rs.
                                        6.Black Coffee-----> 250 Rs.
                                        7.Milk-----> 130 Rs.
                                        8.Beer-----> 600 Rs.
                                        9.Wisky-----> 650 Rs.""")
                                try:
                                    cid2 = int(input("Enter Cuisine Choice:"))
                                    if cid2==1:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Vegetarian Combo'
                                            restaurentbill = quantity * 300
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                        else:
                                            print("Invalid Input")
                                    elif cid2==2:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Non-Vegetarian Combo'
                                            restaurentbill = quantity * 500
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==3:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Veg & Non-Veg Combo'
                                            restaurentbill = quantity * 750
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==4:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Coffee'
                                            restaurentbill = quantity * 200
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==5:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Tea'
                                            restaurentbill = quantity * 150
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==6:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Black Coffee'
                                            restaurentbill = quantity * 250
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==7:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Milk'
                                            restaurentbill = quantity * 130
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==8:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Beer'
                                            restaurentbill = quantity * 600
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==9:
                                        try:
                                            quantity = int(input("Enter Quantity : "))
                                            dish = 'Wisky'
                                            restaurentbill = quantity * 650
                                            sql = "UPDATE RESTAURENT SET CUISINE_CHOICE=%s,CUISINE=%s,Quantity=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql,(cid2,dish,quantity,restaurentbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    else:
                                        print("Invalid Input")
                                except ValueError:
                                    print("Invalid Input,Please Try Again")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 4:
                    print("You Have selected to Edit a Record In Game Table Details")
                    print("""
                        1--->Edit a Record in Customer ID Details
                        2--->Edit a Record in Order no. Details
                        3--->Edit a Record in GAME Choice,GAME,HOUR No,Bill Details
                                                                                """)
                    try:
                        c = int(input("Enter Your Choice:"))
                        if c == 1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM GAMING WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter New Customer ID:")
                                sql = "UPDATE GAMING SET CID=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 2:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM GAMING WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter Updated OrderNo:")
                                sql = "UPDATE GAMING SET ORDER_NO=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 3:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM GAMING WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                print("""
                                    1. Table Tennis -----> 150 Rs./HR
                                    2. Bowling -----> 100 Rs./HR
                                    3. Cart Racing -----> 250 Rs./HR
                                    4. VR Gaming -----> 400 Rs./HR
                                    5. Video Games -----> 300 Rs./HR
                                    6. Swimming Pool Games -----> 350 Rs./HR
                                    """)
                                try:
                                    cid2 = int(input("Enter Game Choice to edit Game choice,Games,Hours and Bill"))
                                    if cid2==1:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            game = 'Table Tennis'
                                            gamingbill = hour * 150
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==2:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            game = 'Bowling'
                                            gamingbill = hour * 100
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 == 3:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            gamingbill = hour * 250
                                            game = 'Cart Racing'
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 ==4:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            game = 'VR Gaming'
                                            gamingbill = hour * 400
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 ==5:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            game = 'Video Games'
                                            gamingbill = hour * 300
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2 ==6:
                                        try:
                                            hour = int(input("Enter Quantity : "))
                                            game = 'Swimming Pool Games'
                                            gamingbill = hour * 350
                                            sql = "UPDATE GAMING SET GAME_CHOICE=%s,GAMES=%s,HOURS=%s,GAMING_BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2, game, hour, gamingbill, cid))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    else:
                                        print("Invalid Input")
                                except ValueError:
                                    print("Invalid Input,Please Try Again")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 5:
                    print("You Have selected to Edit a Record In Fashion Table Details")
                    print("""
                        1--->Edit a Record in Customer ID Details
                        2--->Edit a Record in Order no. Details
                        3--->Edit a Record in DRESS Choice No,DRESS,QUANTITY,BILL Details                                                                                                                                                   
                                                                                    """)
                    try:
                        c = int(input("Enter Your Choice:"))
                        if c == 1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM FASHION WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter New Customer ID:")
                                sql = "UPDATE FASHION SET CID=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 2:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM FASHION WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                cid2 = input("Enter Updated OrderNo:")
                                sql = "UPDATE FASHION SET ORDER_NO=%s WHERE CID=%s"
                                cursor.execute(sql, (cid2, cid))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 3:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM FASHION WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                print("""
                                           1.Shirts - ----> 1500Rs.
                                           2.T - Shirts - ----> 300Rs.
                                           3.Pants - ----> 2000Rs.
                                           4.Jeans - ----> 4000Rs.
                                           5.Tassel top - ----> 500Rs.
                                           6.Gown - ----> 3000Rs.
                                           7.Western dress - ----> 3000Rs.
                                           8.Skirts - ----> 400Rs.
                                           9.Trousers - ----> 200Rs.
                                           10.InnerWear - ----> 30Rs.
                                                """)
                                try:
                                    cid2 = int(input("Enter Updated Dress Choice to update dress choice, dress, quantity and bill"))
                                    if cid2==1:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Shirts'
                                            fashionbill = quantity * 1500
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==2:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'T-Shirts'
                                            fashionbill = quantity * 300
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==3:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Pants'
                                            fashionbill = quantity * 2000
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==4:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Jeans'
                                            fashionbill = quantity * 4000
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==5:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Tassel top'
                                            fashionbill = quantity * 500
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==6:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Gown'
                                            fashionbill = quantity * 3000
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==7:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Western dress'
                                            fashionbill = quantity * 3000
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==8:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Skirts'
                                            fashionbill = quantity * 400
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==9:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'Trousers'
                                            fashionbill = quantity * 200
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    elif cid2==10:
                                        try:
                                            quantity = int(input("Enter Quantity: "))
                                            dress = 'InnerWear'
                                            fashionbill = quantity * 30
                                            sql = "UPDATE FASHION SET DRESS_CHOICE=%s,DRESS=%s,AMOUNT=%s,BILL=%s WHERE CID=%s"
                                            cursor.execute(sql, (cid2,dress,quantity,fashionbill,cid,))
                                            cursor.execute("COMMIT")
                                            print("Changes are Have Been Made Successfully")
                                        except ValueError:
                                            print("Invalid Input,Please Try Again")
                                    else:
                                        print("Invalid Input")
                                except ValueError:
                                    print("Invalid Input,Please Try Again")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b==6:
                    print("Exiting")
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input Please Try Again")
        elif a==2:
            print("""
                    1--->Delete a Record in Customer Details
                    2--->Delete a Record in Room Details
                    3--->Delete a Record in Restaurent Bill Details
                    4--->Delete a Record in Gaming Details
                    5--->Delete a Record in Fashion Details
                    6--->Delete a Record in Total Bill Details
                    7--->Exit
                                                        """)
            try:
                b = int(input("Enter Your Choice"))
                if b==1:
                    cid = input("Enter Customer ID:")
                    sql0 = "SELECT CID FROM C_DETAILS WHERE CID=%s"
                    cursor.execute(sql0, (cid,))
                    data = cursor.fetchall()
                    try:
                        b = data[0][0]
                    except IndexError:
                        b = ['null']
                    if cid == b:
                        sql = "DELETE FROM C_DETAILS WHERE CID=%s"
                        cursor.execute(sql, (cid,))
                        cursor.execute("COMMIT")
                        print("Changes are Have Been Made Successfully")
                    else:
                        print("Record You are Trying to Modify doesnt exist")
                elif b==2:
                    cid = input("Enter Customer ID:")
                    sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
                    cursor.execute(sql0, (cid,))
                    data = cursor.fetchall()
                    try:
                        b = data[0][0]
                    except IndexError:
                        b = ['null']
                    if cid == b:
                        sql = "DELETE FROM ROOM_RENT WHERE CID=%s"
                        cursor.execute(sql, (cid,))
                        cursor.execute("COMMIT")
                        print("Changes are Have Been Made Successfully")
                    else:
                        print("Record You are Trying to Modify doesnt exist")
                elif b==3:
                    print("""
                        1--->Delete a Record in Restaurent Details Using Customer ID
                        2--->Delete a Record in Restaurent Details Using Order NO
                        """)
                    try:
                        c=int(input("Enter Your Choice:"))
                        if c==1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM Restaurent WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                sql = "DELETE FROM Restaurent WHERE CID=%s"
                                cursor.execute(sql, (cid,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==2:
                            Order = input("Enter OrderNO.:")
                            sql0 = "SELECT CID FROM Restaurent WHERE ORDER_NO=%s"
                            cursor.execute(sql0, (Order,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if  Order == b:
                                sql = "DELETE FROM Restaurent WHERE ORDER_NO=%s"
                                cursor.execute(sql, (Order,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b==4:
                    print("""
                        1--->Delete a Record in Gaming Details Using Customer ID
                        2--->Delete a Record in Gaming Details Using Order NO
                        """)
                    try:
                        c=int(input("Enter Your Choice:"))
                        if c==1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM Gaming WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                sql = "DELETE FROM Gaming WHERE CID=%s"
                                cursor.execute(sql, (cid,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c==2:
                            Order = input("Enter OrderNO.:")
                            sql0 = "SELECT CID FROM Gaming WHERE ORDER_NO=%s"
                            cursor.execute(sql0, (Order,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if Order == b:
                                sql = "DELETE FROM Gaming WHERE ORDER_NO=%s"
                                cursor.execute(sql, (Order,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input,Please Try Again")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 5:
                    print("""
                        1--->Delete a Record in Clothing Details Using Customer ID
                        2--->Delete a Record in Clothing Details Using Order NO
                        """)
                    try:
                        c = int(input("Enter Your Choice:"))
                        if c == 1:
                            cid = input("Enter Customer ID:")
                            sql0 = "SELECT CID FROM FASHION WHERE CID=%s"
                            cursor.execute(sql0, (cid,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if cid == b:
                                sql = "DELETE FROM FASHION WHERE CID=%s"
                                cursor.execute(sql, (cid,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        elif c == 2:
                            Order = input("Enter OrderNO.:")
                            sql0 = "SELECT CID FROM FASHION WHERE ORDER_NO=%s"
                            cursor.execute(sql0, (Order,))
                            data = cursor.fetchall()
                            try:
                                b = data[0][0]
                            except IndexError:
                                b = ['null']
                            if Order == b:
                                sql = "DELETE FROM FASHION WHERE ORDER_NO=%s"
                                cursor.execute(sql, (Order,))
                                cursor.execute("COMMIT")
                                print("Changes are Have Been Made Successfully")
                            else:
                                print("Record You are Trying to Modify doesnt exist")
                        else:
                            print("Invalid Input")
                    except ValueError:
                        print("Invalid Input,Please Try Again")
                elif b == 6:
                    cid = input("Enter Customer ID:")
                    sql0 = "SELECT CID FROM TOTAL WHERE CID=%s"
                    cursor.execute(sql0, (cid,))
                    data = cursor.fetchall()
                    try:
                        b = data[0][0]
                    except IndexError:
                        b = ['null']
                    if cid == b:
                        sql = "DELETE FROM TOTAL WHERE CID=%s"
                        cursor.execute(sql, (cid,))
                        cursor.execute("COMMIT")
                        print("Changes are Have Been Made Successfully")
                    else:
                        print("Record You are Trying to Modify doesnt exist")
                elif b==7:
                    print("Exiting")
                else:
                    print("Invalid Input,Please Try Again")
            except ValueError:
                print("Invalid Input,Please Try Again")
        elif a == 3:
            print("Exiting")
        else:
            print("Invalid Input,Please Try Again")
    except ValueError:
        print("Invalid Input,Please Try Again")