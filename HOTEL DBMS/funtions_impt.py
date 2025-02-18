from datetime import datetime
cid0=''

def MYSQLconnection(connection):
    myConnection=connection
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()

def create_tables(connection):
    myConnection = connection
    cursor = myConnection.cursor()
    cursor.execute("use HMS")
    c_details = """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20) primary key,
            C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),
            C_EMAIL VARCHAR(30))"""
    cursor.execute(c_details)
    room = """CREATE TABLE IF NOT EXISTS ROOMS(R_NO VARCHAR(20) primary key,Room_Type VARCHAR(30)
                ,COST INT,STATUS VARCHAR(1))"""
    cursor.execute(room)
    ROOM_RENT = """CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20) primary key,CHECK_IN DATE,CHECK_OUT DATE,
            ROOM_QUALITY VARCHAR(30),NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"""
    cursor.execute(ROOM_RENT)
    FOOD = """CREATE TABLE IF NOT EXISTS FOOD(ID VARCHAR(20) primary key,CUISINE_Type VARCHAR(30),CUISINE VARCHAR(30)
            ,COST VARCHAR(30))"""
    cursor.execute(FOOD)
    RESTAURENT = """CREATE TABLE IF NOT EXISTS RESTAURENT(ORDER_NO VARCHAR(20) primary key,CID VARCHAR(20),
            CUISINE_Choice VARCHAR(30),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"""
    cursor.execute(RESTAURENT)
    cursor.execute("""CREATE TABLE IF NOT EXISTS FASHION(ORDER_NO VARCHAR(20) primary key,CID VARCHAR(20),
            DRESS_CHOICE VARCHAR(30),DRESS VARCHAR(30),AMOUNT VARCHAR(30),BILL VARCHAR(30))""")
    TOTALBill = """CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20) primary key,C_NAME VARCHAR(30),ROOMRENT INT ,
            RESTAURENTBILL INT ,GAMINGBILL INT,FASHIONBILL INT,TOTALAMOUNT INT)"""
    cursor.execute(TOTALBill)
    GAMING = """CREATE TABLE IF NOT EXISTS GAMING(ORDER_NO VARCHAR(20) primary key,CID VARCHAR(20),
               GAME_CHOICE VARCHAR(30),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"""
    cursor.execute(GAMING)
    cursor.close()

def userEntry(connection):
    myConnection = connection#importing mysql credentials from class_cid
    if myConnection:
        while True:
            cursor=myConnection.cursor()
            cid = input("Please Enter Customer Identification Number : ")
            sql0="SELECT CID FROM C_DETAILS WHERE CID=%s"#1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0,(cid,))
            data=cursor.fetchall()
            try:        #using try and except method to check if any data is present in the tables
                b=data[0][0]
            except IndexError:
                b=['null']
            if cid==b:
                print("This CID Already Exists")
                #2Checking if The CID already exists to avoid duplication/errors using if/else
            else:
                #all user inputing customer details
                name = input("Enter Customer Name : ")
                address = input("Enter Customer Address : ")
                age= input("Enter Customer Age : ")
                nationality = input("Enter Customer Country : ")
                phoneno= input("Enter Customer Contact Number : ")
                if len(phoneno)!=10:
                    print("Wrong contact Info entered , Please enter correct information")
                    continue
                email = input("Enter Customer Email : ")
                if not email.endswith('@gmail.com'):
                    email=email+"@gmail.com"

                sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"#place holder for variables
                values= (cid,name,address,age,nationality,phoneno,email)#storing all user inputs in a single variable
                cursor.execute(sql,values)#executing the place holder and the values
                cursor.execute("COMMIT")#commiting the statement so that all values will be stored in database
                print("\nNew Customer Entered In The System Successfully !")
                cursor.close()
                return False
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def searchCustomer(connection):
    myConnection = connection
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("ENTER CUSTOMER ID : ")
        global cid0
        cid0=cid
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            for rows in data:
                print("CID=", rows[0], ",NAME=", rows[1], ",Address=", rows[2], ",AGE=", rows[3], ",Country=", rows[4],
                    ",PHONE no=", rows[5], ",Email=", rows[6], "\n")
                cursor.close()
                return True
        else:
            print("No Record With CID=",cid,"exists")
            cursor.close()
            return False
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

#More Improvement can be made
def roomRent(connection):
    myConnection = connection  # importing mysql credentials from class_cid
    cursor = myConnection.cursor()
    sql = "SELECT * FROM ROOMS ORDER BY ROOM_Type"
    cursor.execute(sql)
    roomdata = cursor.fetchall()
    if not roomdata:
        print("No Room Details")
        print("Please Fill Up Room Details First")
        exit()
    customer = searchCustomer(connection)
    if customer:
        while True:
            cid = cid0
            sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0, (cid,))
            data = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                b = data[0][0]
            except IndexError:
                b = ['null']
            if cid == b:
                print("This CID Already Exist")
                continue
                # 2Checking if The CID already exists to avoid duplication/errors using if/else
            else:
                print("    ### ROOM DETAILS ###")
                for rows in roomdata:
                    print("R_NO =", rows[0], "\t\tROOM Type =", rows[1], "\t\tCOST =", rows[2], "\t\tSTATUS =",
                          rows[3], "\n")
                R_No= input("Enter Food ID Selected By Customer:")
                if (len(R_No)==0):
                    print("Room No. Cannot be Empty")
                    continue
                sql0 = "SELECT R_NO,STATUS FROM ROOMS WHERE R_NO=%s"  # 1Checking if The ID already exists to avoid duplication/errors
                cursor.execute(sql0, (R_No,))
                rdata = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = rdata[0][0]
                    bb= rdata[0][1]
                except IndexError:
                    b = ['null']
                    bb= ['null']
                if (R_No != b):
                    print("Room Number Doesnt Exist")
                    continue
                if (bb=='O'):
                    print("The Room is Currently Occupied")
                    continue
                try:
                    checkin = input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
                    checkout = input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
                    datetime.strptime(checkin,"%Y-%m-%d")
                    datetime.strptime(checkout, "%Y-%m-%d")
                except ValueError:
                    print("Incorrect DateTime Format")
                    continue
                checkin=datetime.strptime(checkin, "%Y-%m-%d")
                checkout=datetime.strptime(checkout, "%Y-%m-%d")
                quantity=checkin-checkout
                sql0 = "SELECT * FROM ROOMS WHERE R_NO=%s"
                cursor.execute(sql0, (R_No,))
                rooomdata0=cursor.fetchall()
                room_type=rooomdata0[0][1]
                roomrent = int(rooomdata0[0][2]) * quantity
                cid = cid0
                sql = "INSERT INTO ROOMS VALUES(%s,%s,%s,%s,%s,%s)"  # place holder for variables
                print(cid)
                values = (cid,checkin,checkout,room_type,quantity, R_No,roomrent,)
                # storing all variables in a single variable
                cursor.execute(sql, values)
                stat='O'
                cursor.execute("COMMIT")
                sql = "UPDATE ROOMS SET STATUS=%s WHERE R_NO=%s"
                cursor.execute(sql, (stat, R_No))
                cursor.execute("COMMIT")
                sql2 = "SELECT CID,CHECK_IN,CHECK_OUT,NO_OF_DAYS,ROOMNO,ROOMRENT FROM RESTAURENT WHERE ORDER_NO= %s"
                cursor.execute(sql2, (cid,))
                data = cursor.fetchall()  # fetching cuisine,quantiity and bills
                a = data[0][0]
                # data[0][0] means its fetching a string from a list of tuples stored in variable data
                b = data[0][1]
                c = data[0][2]
                d = data[0][3]
                e = data[0][4]
                f = data[0][5]
                print("\n\n#################################################")
                print("Customer Room details as in Below")
                print("CID =", a)
                print("CHECK-IN Date=", b)
                print("CHECK-OUT Date=", c)
                print("ROOM_QUALITY=", d)
                print("NO OF DAYS=", e)
                print("Room Bill=", f)
                print("\n\n#################################################")
                cursor.close()
                return False
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def view_inout(connection):
    myConnection = connection#importing mysql credentials from class_cid
    customer=searchCustomer(connection)
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = cid0
            sql0 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0, (cid,))
            data = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                b = data[0][0]
            except IndexError:
                b = ['null']
            if cid != b:
                print("No Records For CID=", cid, " In CheckIN and CheckOUT Records")
            else:
                sql01 = "SELECT * FROM ROOM_RENT WHERE CID=%s"
                cursor.execute(sql01, (cid,))
                data=cursor.fetchall()
                for rows in data:
                    print("CID=", rows[0], ",CHECKIN DATE=", rows[1], ",CHECKOUT DATE=", rows[2], ",ROOM QUALITY=",
                          rows[3], ",NO OF DAYS=", rows[4],",Room NO=", rows[5], ",Room Rent=", rows[6], "\n")
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def Restaurent(connection):
    myConnection = connection  # importing mysql credentials from class_cid
    cursor = myConnection.cursor()
    sql = "SELECT * FROM FOOD ORDER BY CUISINE_TYPE"
    cursor.execute(sql)
    fooddata = cursor.fetchall()
    if not fooddata:
        print("No Food Details")
        exit()
    customer = searchCustomer(connection)
    if customer:
        sql01 = "SELECT CID FROM room_rent WHERE CID=%s"
        cid = cid0
        cursor.execute(sql01, (cid,))
        p = cursor.fetchall()
        if not p:
            print("Please Fill Up CheckIn and CheckOUT details for Customer ID=", cid, " before Accessing this Tab")
            exit()
        q = p[0][0]
        if q != cid0:
            print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Restaurent")
            exit()

        while True:
            order = input("Please Enter Order Number:")
            sql0 = "SELECT ORDER_NO FROM Restaurent WHERE ORDER_NO=%s"
            # 1Checking if The order already exists to avoid duplication/errors
            cursor.execute(sql0, (order,))
            x = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                y = x[0][0]
            except IndexError:
                y = ['null']
            if order == y:
                print("OrderNO. Already Exists")  # 2Checking if The order already exists to avoid duplication/errors using if/else
                continue
            else:
                print("       ### Food Menu ###")
                for rows in fooddata:
                    print("ID =", rows[0], "\t\tDISH Type =", rows[1], "\t\tDISH/BEVERAGE =", rows[2], "\t\tBILL =",
                          rows[3], "\n")
                foodid = input("Enter Food ID Selected By Customer:")
                if (len(foodid)==0):
                    print("Food Id Cannot be Empty")
                    continue
                sql0 = "SELECT ID FROM FOOD WHERE ID=%s"  # 1Checking if The ID already exists to avoid duplication/errors
                cursor.execute(sql0, (foodid,))
                fdata = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = fdata[0][0]
                except IndexError:
                    b = ['null']
                if foodid != b:
                    print("ID Does'nt Exist")
                    continue
                try:
                    quantity=int(input("Enter Food Quantity"))
                except ValueError:
                    print("Incorrect Food Quantity Value")
                    continue
                sql0 = "SELECT * FROM FOOD WHERE ID=%s"
                cursor.execute(sql0, (foodid,))
                fooodata0=cursor.fetchall()
                choice_dish=fooodata0[0][1]
                dish = fooodata0[0][2]
                restaurentbill = int(fooodata0[0][3]) * quantity
                cid = cid0
                sql = "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s,%s,%s)"  # place holder for variables
                print(cid)
                values = (order, cid, choice_dish, dish, quantity, restaurentbill)
                # storing all variables in a single variable
                cursor.execute(sql, values)
                cursor.execute("COMMIT")
                sql2 = "SELECT CUISINE,QUANTITY,BILL FROM RESTAURENT WHERE ORDER_NO= %s"
                cursor.execute(sql2, (order,))
                data = cursor.fetchall()  # fetching cuisine,quantiity and bills
                a = data[0][0]
                # data[0][0] means its fetching a string from a list of tuples stored in variable data
                b = data[0][1]
                c = data[0][2]
                print("\n\n#################################################")
                print("Order details as in Below")
                print("Cuisine=", a)
                print("Quantity=", b)
                print("Bill=", c)
                print("Your Total Bill Amount Is : Rs. ", restaurentbill)
                print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
                print("\n\n#################################################")
                cursor.close()
                return False

def view_rest(connection):
    myConnection = connection#importing mysql credentials from class_cid
    customer=searchCustomer(connection)
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid=cid0
            sql0 = "SELECT CID FROM Restaurent WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0, (cid,))
            data = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                b = data[0][0]
            except IndexError:
                b = ['null']
            if cid != b:
                print("No Records For CID=",cid," In Restaurent Details")
            else:
                sql1 = "SELECT * FROM RESTAURENT WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
                cursor.execute(sql1, (cid,))
                data = cursor.fetchall()
                for rows in data:
                    print("CID=", rows[1],"ORDERNO.=", rows[0],",DISH/BEVERAGE=", rows[3], ",QUANTITY=", rows[4],
                          ",BILL=", rows[5], "\n")
                sql2 = "SELECT BILL FROM RESTAURENT WHERE CID= %s"
                cursor.execute(sql2, (cid,))
                data2 = cursor.fetchall()
                restaurentbill3 = 0
                restaurentbill1 = [i[0] for i in data2]
                restaurentbill2 = list(map(int, restaurentbill1))
                for i in range(0, len(restaurentbill2)):
                    restaurentbill3 = restaurentbill3 + restaurentbill2[i]
                print("Customer's Total Restaurent Bill is",restaurentbill3)
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#NEED REWORK AND EXTRA GAMINGS FUNTION
def Gaming(connection):

    myConnection = connection
    customer = searchCustomer(connection)
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql01 = "SELECT CID FROM room_rent WHERE CID=%s"
            cid = cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Gaming Arcade")
            else:
                q = p[0][0]
                if q != cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Gaming Arcade")
                else:
                    while True:
                        order = input("Please Enter Order Number:")
                        sql0 = "SELECT ORDER_NO FROM GAMING WHERE ORDER_NO=%s"
                        cursor.execute(sql0, (order,))
                        x = cursor.fetchall()
                        try:
                            y = x[0][0]
                        except IndexError:
                            y = ['null']
                        if order == y:
                            print("OrderNO. Already Exists")
                            continue
                        else:
                            print("""
                            ##### CMR HOTELS GAMING HUB #####
                            1. Table Tennis -----> 150 Rs./HR
                            2. Bowling -----> 100 Rs./HR
                            3. Cart Racing -----> 250 Rs./HR
                            4. VR Gaming -----> 400 Rs./HR
                            5. Video Games -----> 300 Rs./HR
                            6. Swimming Pool Games -----> 350 Rs./HR
                            7. Exit
                            """)
                            try:
                                gamechoice = int(input("Enter What Game The Customer wants To Play : "))
                                try:
                                    hour = int(input("Enter No Of Hours The Customer wants To Play : "))
                                    print("\n\n#################################################")
                                    if gamechoice == 1:
                                        print("The Customer Has SELECTED TO PLAY : Table Tennis")
                                        game = 'Table Tennis'
                                        gamingbill = hour * 150
                                    elif gamechoice == 2:
                                        print("The Customer Has SELECTED TO PLAY : Bowling")
                                        game = 'Bowling'
                                        gamingbill = hour * 100
                                    elif gamechoice == 3:
                                        print("The Customer Has SELECTED TO PLAY : Cart Racing")
                                        game = 'Cart Racing'
                                        gamingbill = hour * 250
                                    elif gamechoice == 4:
                                        print("The Customer Has SELECTED TO PLAY : VR Gaming")
                                        game = 'VR Gaming'
                                        gamingbill = hour * 400
                                    elif gamechoice == 5:
                                        print("The Customer Has SELECTED TO PLAY : Video Games")
                                        game = 'Video Games'
                                        gamingbill = hour * 300
                                    elif gamechoice == 6:
                                        print("The Customer Has SELECTED TO PLAY : Swimming Pool Games")
                                        game = 'Swimming Pool Games'
                                        gamingbill = hour * 350
                                    elif gamechoice == 7:
                                        print('\nHope The Customer Visits Again')
                                        game = 'none'
                                        gamingbill = 0
                                    else:
                                        print("Invalid Input, Please Try Again")
                                        return
                                    cid = cid0
                                    sql = "INSERT INTO GAMING VALUES(%s,%s,%s,%s,%s,%s)"
                                    values = (order, cid, gamechoice, game, hour, gamingbill)
                                    cursor.execute(sql, values)
                                    cursor.execute("COMMIT")
                                    sql2 = "SELECT GAMES,HOURS,GAMING_BILL FROM GAMING WHERE ORDER_NO= %s"
                                    cursor.execute(sql2, (order,))
                                    data1 = cursor.fetchall()
                                    a = data1[0][0]
                                    b = data1[0][1]
                                    c = data1[0][2]
                                    print("\n\n#################################################")
                                    print("Order details as in Below")
                                    print("Game=", a)
                                    print("Hours=", b)
                                    print("Bill=", c)
                                    print("Your Gaming Bill Is : Rs. ", gamingbill)
                                    print("\n *** WE HOPE The Customer WILL ENJOY The CustomerR GAME ***")
                                    print("\n\n#################################################")
                                    cursor.close()
                                except ValueError:
                                    print("Invalid Input, Please Try Again")
                            except ValueError:
                                print("Invalid Input, Please Try Again")
                            return False
        else:
            print("ERROR ESTABLISHING MYSQL CONNECTION!")

def view_gaming(connection):
    myConnection = connection#importing mysql credentials from class_cid
    customer=searchCustomer(connection)
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = cid0
            sql0 = "SELECT CID FROM Gaming WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0, (cid,))
            data = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                b = data[0][0]
            except IndexError:
                b = ['null']
            if cid != b:
                print("No Records For CID=", cid, " In Gaming Records")
            else:
                sql01 = "SELECT * FROM Gaming WHERE CID=%s"
                cursor.execute(sql01, (cid,))
                data=cursor.fetchall()
                for rows in data:
                    print("CID=", rows[1],"ORDERNO.=", rows[0],",Games=", rows[3], ",Hours=", rows[4],
                          ",BILL=", rows[5], "\n")
                sql4 = "SELECT GAMING_BILL FROM GAMING WHERE CID= %s"
                cursor.execute(sql4, (cid,))
                data4 = cursor.fetchall()
                gamingbill3 = 0
                gamingbill1 = [i[0] for i in data4]
                gamingbill2 = list(map(int, gamingbill1))
                for i in range(0, len(gamingbill2)):
                    gamingbill3 = gamingbill3 + gamingbill2[i]
                print("Customer's Total Gaming Bill is",gamingbill3)
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#NEED REWORK AND EXTRA CLOTH FUNCTION
def Fashion(connection):
    myConnection = connection
    customer = searchCustomer(connection)
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql01 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
            cid = cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Fashion store")
            else:
                q = p[0][0]
                if q != cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Fashion store")
                else:
                    while True:
                        order = input("Please Enter Order no: ")
                        sql0 = "SELECT CID FROM FASHION WHERE ORDER_NO=%s"
                        cursor.execute(sql0, (order,))
                        x = cursor.fetchall()
                        try:
                            y = x[0][0]
                        except IndexError:
                            y = ['null']
                        if order == y:
                            print("OrderNO. Already Exists")
                            continue
                        else:
                            print("""
                            ##### CMR HOTELS FASHION STORE #####
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
                            11.Not Interested
                            """)
                            try:
                                dresschoice=int(input("Please Enter The Customer's Choice: "))
                                try:
                                    quantity=int(input("Please Enter The Quantity: "))
                                    if type(quantity)==int:
                                        if dresschoice==1:
                                            print("\nThe Customer Has purchased -----> Shirts")
                                            dress = 'Shirts'
                                            fashionbill = quantity * 1500
                                        elif dresschoice==2:
                                            print("\nThe Customer Has purchased -----> T-Shirts")
                                            dress = 'T-Shirts'
                                            fashionbill = quantity * 300
                                        elif dresschoice==3:
                                            print("\nThe Customer Has purchased -----> Pants")
                                            dress = 'Pants'
                                            fashionbill = quantity * 2000
                                        elif dresschoice==4:
                                            print("\nThe Customer Has purchased -----> Jeans")
                                            dress = 'Jeans'
                                            fashionbill = quantity * 4000
                                        elif dresschoice==5:
                                            print("\nThe Customer Has purchased -----> Tassel top")
                                            dress = 'Tassel top'
                                            fashionbill = quantity * 500
                                        elif dresschoice==6:
                                            print("\nThe Customer Has purchased -----> Gown")
                                            dress = 'Gown'
                                            fashionbill = quantity * 3000
                                        elif dresschoice==7:
                                            print("\nThe Customer Has purchased -----> Western dress")
                                            dress = 'Western dress'
                                            fashionbill = quantity * 3000
                                        elif dresschoice==8:
                                            print("\nThe Customer Has purchased -----> Skirts")
                                            dress = 'Skirts'
                                            fashionbill = quantity * 400
                                        elif dresschoice==9:
                                            print("\nThe Customer Has purchased -----> Trousers")
                                            dress = 'Trousers'
                                            fashionbill = quantity * 200
                                        elif dresschoice==10:
                                            print("\nThe Customer Has purchased -----> InnerWear")
                                            dress = 'InnerWear'
                                            fashionbill = quantity * 30
                                        elif dresschoice==11:
                                            print("\nHope You Find Something better next Time , Please Visit Again")
                                            dress = 'none'
                                            fashionbill = quantity * 0
                                        else:
                                            print("Invalid Input, Please Try Again")
                                            return
                                        sql = "INSERT INTO FASHION VALUES(%s,%s,%s,%s,%s,%s)"
                                        cid = cid0
                                        values = (order, cid, dresschoice, dress, quantity, fashionbill)
                                        cursor.execute(sql, values)
                                        cursor.execute("COMMIT")
                                        sql2 = "SELECT DRESS,AMOUNT,BILL FROM FASHION WHERE ORDER_NO= %s"
                                        cursor.execute(sql2, (order,))
                                        data = cursor.fetchall()
                                        a = data[0][0]
                                        b = data[0][1]
                                        c = data[0][2]
                                        print("\n\n#################################################")
                                        print("Order details as in Below")
                                        print("Dress=", a)
                                        print("Quantity=", b)
                                        print("Bill=", c)
                                        print("\nYour Total Clothing Bill Is : ", fashionbill)
                                        print("\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!")
                                        print("\n\n#################################################")
                                        cursor.close()
                                except ValueError:
                                    print('Invalid Input,Please Try Again')
                            except ValueError:
                                print('Invalid Input,Please Try Again')
                            return False
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def view_fashion(connection):

    myConnection = connection#importing mysql credentials from class_cid
    customer=searchCustomer(connection)
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid=cid0
            sql0 = "SELECT CID FROM Fashion WHERE CID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0, (cid,))
            data = cursor.fetchall()
            try:  # using try and except method to check if any data is present in the tables
                b = data[0][0]
            except IndexError:
                b = ['null']
            if cid != b:
                print("No Records For CID=", cid, " In Fashion Details")
            else:
                sql01 = "SELECT * FROM FASHION WHERE CID=%s"
                cursor.execute(sql01, (cid,))
                data=cursor.fetchall()
                for rows in data:
                    print("CID=", rows[1],"ORDERNO.=", rows[0],",Cloth", rows[3], ",QUANTITY=", rows[4],
                          ",BILL=", rows[5], "\n")
                sql3 = "SELECT BILL FROM FASHION WHERE CID= %s"
                cursor.execute(sql3, (cid,))
                data3 = cursor.fetchall()
                fashionbill3 = 0
                fashionbill1 = [i[0] for i in data3]
                fashionbill2 = list(map(int, fashionbill1))
                for i in range(0, len(fashionbill2)):
                    fashionbill3 = fashionbill3 + fashionbill2[i]
                print("The Customer's Total Clothing Bill is",fashionbill3)
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def totalAmount(connection):
    customer=searchCustomer(connection)
    if customer:
        myConnection = connection
        if myConnection:
            cursor=myConnection.cursor()
            sql01 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
            cid = cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Total Bill Section")
            else:
                q = p[0][0]
                if q != cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Total Bill Section")
                else:
                    sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    cid=cid0
                    sql0 = "SELECT CID FROM TOTAL WHERE CID=%s"
                    cursor.execute(sql0, (cid,))
                    data = cursor.fetchall()
                    try:
                        b = data[0][0]
                    except IndexError:
                        b = ['null']
                    if cid == b:
                        print("Total Bill For This CID already exists")
                        print("\nPlease Refer To Option-9-OLD BILL to View The Bill Corresponded To The CID")
                    else:
                        cid2=cid0
                        name = input("Enter Customer Name : ")
                        roomrent3=0
                        restaurentbill3=0
                        fashionbill3=0
                        gamingbill3=0
                        sql1 = "SELECT ROOMRENT FROM ROOM_RENT WHERE CID= %s"
                        cursor.execute(sql1, (cid2,))
                        data = cursor.fetchall()
                        roomrent1 = [i[0] for i in data]
                        roomrent2 = list(map(int, roomrent1))
                        for i in range(0, len(roomrent2)):
                            roomrent3 = roomrent3 + roomrent2[i]
                        sql2 = "SELECT BILL FROM RESTAURENT WHERE CID= %s"
                        cursor.execute(sql2, (cid2,))
                        data1 = cursor.fetchall()
                        restaurentbill1 = [i[0] for i in data1]
                        restaurentbill2 = list(map(int, restaurentbill1))
                        for i in range(0, len(restaurentbill2)):
                            restaurentbill3 = restaurentbill3 + restaurentbill2[i]
                        sql3 = "SELECT BILL FROM FASHION WHERE CID= %s"
                        cursor.execute(sql3, (cid2,))
                        data3 = cursor.fetchall()
                        fashionbill1 = [i[0] for i in data3]
                        fashionbill2 = list(map(int, fashionbill1))
                        for i in range(0, len(fashionbill2)):
                            fashionbill3 = fashionbill3 + fashionbill2[i]
                        sql4 = "SELECT GAMING_BILL FROM GAMING WHERE CID= %s"
                        cursor.execute(sql4, (cid2,))
                        data4= cursor.fetchall()
                        gamingbill1 = [i[0] for i in data4]
                        gamingbill2 = list(map(int, gamingbill1))
                        for i in range(0, len(gamingbill2)):
                            gamingbill3 = gamingbill3 + gamingbill2[i]
                        grandTotal=roomrent3 + restaurentbill3 + fashionbill3 + gamingbill3
                        values= (cid2,name,roomrent3,restaurentbill3 , gamingbill3,fashionbill3,grandTotal)
                        cursor.execute(sql,values)
                        cursor.execute("COMMIT")
                        cursor.close()
                        print("\n\n#################################################")
                        print("\n **** CMR HOTELS **** CUSTOMER BIlLING ****")
                        print("\n CUSTOMER NAME : " ,name)
                        print("\nROOM RENT : Rs. ",roomrent3)
                        print("\nRESTAURENT BILL : Rs. ",restaurentbill3)
                        print("\nFASHION BILL : Rs. ",fashionbill3)
                        print("\nGAMING BILL : Rs. ",gamingbill3)
                        print("___________________________________________________")
                        print("\nTOTAL AMOUNT : Rs. ",grandTotal)
                        print("\n\n#################################################")
                        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def searchOldBill(connection):
    myConnection =connection
    customer=searchCustomer(connection)
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = cid0
            roomrent3 = 0
            restaurentbill3 = 0
            fashionbill3 = 0
            gamingbill3 = 0
            sql1 = "SELECT ROOMRENT FROM ROOM_RENT WHERE CID= %s"
            cursor.execute(sql1, (cid,))
            data = cursor.fetchall()
            roomrent1 = [i[0] for i in data]
            roomrent2 = list(map(int, roomrent1))
            for i in range(0, len(roomrent2)):
                roomrent3 = roomrent3 + roomrent2[i]
            sql2 = "SELECT BILL FROM RESTAURENT WHERE CID= %s"
            cursor.execute(sql2, (cid,))
            data1 = cursor.fetchall()
            restaurentbill1 = [i[0] for i in data1]
            restaurentbill2 = list(map(int, restaurentbill1))
            for i in range(0, len(restaurentbill2)):
                restaurentbill3 = restaurentbill3 + restaurentbill2[i]
            sql3 = "SELECT BILL FROM FASHION WHERE CID= %s"
            cursor.execute(sql3, (cid,))
            data3 = cursor.fetchall()
            fashionbill1 = [i[0] for i in data3]
            fashionbill2 = list(map(int, fashionbill1))
            for i in range(0, len(fashionbill2)):
                fashionbill3 = fashionbill3 + fashionbill2[i]
            sql4 = "SELECT GAMING_BILL FROM GAMING WHERE CID= %s"
            cursor.execute(sql4, (cid,))
            data4 = cursor.fetchall()
            gamingbill1 = [i[0] for i in data4]
            gamingbill2 = list(map(int, gamingbill1))
            for i in range(0, len(gamingbill2)):
                gamingbill3 = gamingbill3 + gamingbill2[i]
            sql="SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql,(cid,))
            data=cursor.fetchall()
            if data:
                for rows in data:
                    print("CID=", rows[0], ",NAME=", rows[1])
                    print("\nROOM RENT : Rs. ", roomrent3)
                    print("\nRESTAURENT BILL : Rs. ", restaurentbill3)
                    print("\nFASHION BILL : Rs. ", fashionbill3)
                    print("\nGAMING BILL : Rs. ", gamingbill3)
                    print("\nTOTAL BILL==", rows[6])
            else:
                print("Record Does Not Exist Try Again !")

            cursor.close()
        else:
            print("\nSomething Went Wrong ,Please Try Again !")

def all_cus_det(connection):
    try:
        myConnection = connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM C_DETAILS"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("CID=", rows[0], ",NAME=", rows[1], ",Address=", rows[2], ",AGE=", rows[3], ",Country=", rows[4],
                      ",PHONE no=", rows[5], ",Email=", rows[6], "\n")
        cursor.close()
    except Exception as e:
        print("an error has occured")

def all_bk(connection):
    try:
        myConnection = connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM ROOM_RENT"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("CID=", rows[0], ",CHECKIN DATE=", rows[1], ",CHECKOUT DATE=",rows[2],",ROOM QUALITY=",rows[3],
                      ",NO OF DAYS=",rows[4],",Room NO=",rows[5],",Room Rent=",rows[6],"\n")
        cursor.close()
    except Exception as e:
        print("an error has occured",)

def all_restbill_det(connection):

    try:
        myConnection = connection
        cursor =myConnection.cursor()
        sql = "SELECT * FROM RESTAURENT"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("ORDERNO.=", rows[0], ",CID=", rows[1], ",DISH/BEVERAGE=", rows[3], ",QUANTITY=", rows[4],
                    ",BILL=", rows[5], "\n")
        cursor.close()
    except Exception:
        print("An unexpected error has occured")

def allgame_bill(connection):
    try:
        myConnection= connection
        cursor=myConnection.cursor()
        sql = "SELECT * FROM GAMING"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("ORDERNO.=", rows[0], ",CID=", rows[1], ",GAMES=", rows[3], ",HOURS=", rows[4], ",BILL=", rows[5], "\n")
        cursor.close()
    except Exception:
        print("an error has occured")

def all_fasbill(connection):
    try:
        myConnection = connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM FASHION"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("ORDERNO.=", rows[0], ",CID=", rows[1], ",DRESS=", rows[3], ",QUANTITY=", rows[4],
                      ",BILL=", rows[5], "\n")
        cursor.close()
    except Exception:
        print("an error has occured")

def alltotbill(connection):
    try:
        myConnection = connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM TOTAL"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("CID=", rows[0], "NAME=", rows[1], "ROOMRENT=", rows[2], "RESTAURENT BILL=", rows[3],
                      "GAMING BILL==", rows[4], "FASHION BILL==", rows[5], "TOTAL BILL==", rows[6], "\n")
        cursor.close()
    except Exception:
        print("an error has occured")

#NEEDS TO BE UPDATED
def altdel_rec(connection):
    myConnection =connection
    cursor = myConnection.cursor()
    print("""
        1--->Alter/Edit Record
        2--->Delete Record
        3--->Exit""")
    try:
        a=int(input("Enter Your Choice"))
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

def food(connection):
    myConnection = connection
    cursor = myConnection.cursor()
    while True:
        print("""
                1--->To Check Cuisine Details
                2--->To Enter New Cuisine Details
                3--->To Edit Existing Cuisine Details
                4--->To Delete Existing Cuisine Details
                5--->To Exit
                """)
        try:
            cch = int(input("Enter Your Choice:"))
            if (cch==1):
                sql = "SELECT * FROM FOOD Order by Cuisine_Type"
                cursor.execute(sql)
                data = cursor.fetchall()
                if not data:
                    print("No Existing Record")
                else:
                    for rows in data:
                        print("ID =",rows[0],"\t\tDISH Type =",rows[1],"\t\tDISH/BEVERAGE =",rows[2],"\t\tBILL =", rows[3], "\n")
            elif (cch==2):
                id = input("Please Enter FOOD Identification Number : ")
                if (len(id) == 0):
                    print("Invalid Input")
                    continue
                sql0 = "SELECT ID FROM FOOD WHERE ID=%s"  # 1Checking if The CID already exists to avoid duplication/errors
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    print("This CID Already Exists")
                    # 2Checking if The CID already exists to avoid duplication/errors using if/else
                else:
                    try:
                        fooodtypech=int(input("""
                        1. Vegetarian 
                        2. Non-Vegetarian
                        3. Starters
                        4. Beverages
                        5. Special
                        Enter Choice:"""))
                    except ValueError:
                        print("Incorrect Value")
                        continue
                    if fooodtypech==1:
                        fooodtype = 'Vegetarian'
                    elif fooodtypech==2:
                        fooodtype = 'Non-Vegetarian'
                    elif fooodtypech == 3:
                        fooodtype = 'Starters'
                    elif fooodtypech == 4:
                        fooodtype = 'Beverages'
                    elif fooodtypech == 5:
                        fooodtype = 'Special'
                    else:
                        print("Please Select A Correct Food Type")
                        continue
                    foood = input("Enter Cuisine Name: ")

                    try:
                        cost = int(input("Enter Cuisine Cost: "))
                    except ValueError:
                        print("Invalid Data Entered , Please Enter Cost In Numbers")
                        continue
                    sql = "INSERT INTO FOOD VALUES(%s,%s,%s,%s)"  # place holder for variables
                    values = (id, fooodtype.upper(), foood.upper(), cost)  # storing all user inputs in a single variable
                    cursor.execute(sql, values)  # executing the place holder and the values
                    cursor.execute("COMMIT")  # commiting the statement so that all values will be stored in database
                    print("\nNew Cuisine Has Been Added Succesfully !")
            elif (cch==3):
                id = input("Please Enter FOOD Identification Number : ")
                if (len(id) == 0):
                    print("Invalid Input")
                    continue
                sql0 = "SELECT ID FROM FOOD WHERE ID=%s"  # 1Checking if The ID already exists to avoid duplication/errors
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    try:
                        fooodtypech=int(input("""
                        1. Vegetarian 
                        2. Non-Vegetarian
                        3. Starters
                        4. Beverages
                        5. Special
                        Enter Choice:"""))
                    except ValueError:
                        print("Incorrect Value")
                        continue
                    if fooodtypech==1:
                        fooodtype = 'Vegetarian'
                    elif fooodtypech==2:
                        fooodtype = 'Non-Vegetarian'
                    elif fooodtypech == 3:
                        fooodtype = 'Starters'
                    elif fooodtypech == 4:
                        fooodtype = 'Beverages'
                    elif fooodtypech == 5:
                        fooodtype = 'Special'
                    else:
                        print("Please Select A Correct Food Type")
                        continue
                    foood = input("Enter Cuisine Name: ")
                    try:
                        cost = int(input("Enter Cuisine Cost: "))
                    except ValueError:
                        print("Incorrect Data Type For Cost")
                        continue
                    sql = "UPDATE FOOD SET CUISINE_Type=%s,CUISINE=%s,COST=%s WHERE ID=%s"
                    cursor.execute(sql, (fooodtype, foood, cost,id))
                    cursor.execute("COMMIT")
                    print("Data updated successfully")
                else:
                    print("Identification Number Doesnt Exist")
            elif (cch == 4):
                id = input("Enter ID:")
                sql0 = "SELECT ID FROM FOOD WHERE ID=%s"
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    sql = "DELETE FROM FOOD WHERE ID=%s"
                    cursor.execute(sql, (id,))
                    cursor.execute("COMMIT")
                    print("Changes are Have Been Made Successfully")
                else:
                    print("Record You are Trying to Modify doesnt exist")
            elif (cch==5):
                cursor.close()
                print("Exit")
                break
            else:
                print("Invalid Input")
                continue
        except ValueError:
            print("Invalid Input")
            continue

def rooms(connection):
    myConnection = connection
    cursor = myConnection.cursor()
    while True:
        print("""
                    1--->To Check Room Details
                    2--->To Enter New Room Details
                    3--->To Edit Existing Room Details
                    4--->To Delete Existing Room Details
                    5--->To Exit
                    """)
        try:
            cch = int(input("Enter Your Choice:"))
            if (cch == 1):
                sql = "SELECT * FROM ROOMS ORDER BY ROOM_Type"
                cursor.execute(sql)
                data = cursor.fetchall()
                if not data:
                    print("No Existing Record")
                else:
                    for rows in data:
                        print("R_NO =", rows[0], "\t\tROOM Type =", rows[1], "\t\tCOST =", rows[2], "\t\tSTATUS =",
                              rows[3], "\n")
            elif (cch == 2):
                id = input("Please Enter Room Number : ")
                if (len(id) == 0):
                    print("Invalid Input")
                    continue
                sql0 = "SELECT R_NO FROM ROOMS WHERE R_NO=%s"  # 1Checking if The CID already exists to avoid duplication/errors
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    print("This CID Already Exists")
                    # 2Checking if The CID already exists to avoid duplication/errors using if/else
                else:
                    rooomtype=input("Enter Room Type: ")
                    stat=input("Enter Room Status: ")
                    if (stat!='F' or stat!='Q'):
                        print("Please Enter P OR Q")
                        continue
                    try:
                        cost = int(input("Enter ROOM Rate: "))
                    except ValueError:
                        print("Invalid Data Entered , Please Enter Cost In Numbers")
                        continue
                    sql = "INSERT INTO ROOMS VALUES(%s,%s,%s,%s)"  # place holder for variables
                    values = (id, rooomtype.upper(), cost, stat.upper())  # storing all user inputs in a single variable
                    cursor.execute(sql, values)  # executing the place holder and the values
                    cursor.execute("COMMIT")  # commiting the statement so that all values will be stored in database
                    print("\nNew ROOM DETAILS Has Been Added Succesfully !")
            elif (cch == 3):
                id = input("Please Enter Room Number : ")
                if (len(id) == 0):
                    print("Invalid Input")
                    continue
                sql0 = "SELECT R_NO FROM ROOMS WHERE R_NO=%s"  # 1Checking if The ID already exists to avoid duplication/errors
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:  # using try and except method to check if any data is present in the tables
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    rooomtype=input("Enter Room Type: ")
                    rooomtype=rooomtype.upper()
                    stat = input("Enter Room Status: (O  - occupied / F - Free) ")
                    if len(stat)!=1:
                        print("Enter 1 Character only for room status")
                        continue
                    try:
                        cost = int(input("Enter Room Cost: "))
                    except ValueError:
                        print("Incorrect Data Type For Cost")
                        continue
                    sql = "UPDATE ROOMS SET ROOM_TYPE=%s,COST=%s,STATUS=%s WHERE R_NO=%s"
                    cursor.execute(sql, (rooomtype.upper(), cost, stat.upper(), id))
                    cursor.execute("COMMIT")
                    print("Data updated successfully")
                else:
                    print("Room Number Doesnt Exist")
            elif (cch == 4):
                id = input("Enter ROOM NO:")
                sql0 = "SELECT R_NO FROM ROOMS WHERE R_NO=%s"
                cursor.execute(sql0, (id,))
                data = cursor.fetchall()
                try:
                    b = data[0][0]
                except IndexError:
                    b = ['null']
                if id == b:
                    sql = "DELETE FROM ROOMS WHERE R_NO=%s"
                    cursor.execute(sql, (id,))
                    cursor.execute("COMMIT")
                    print("Changes are Have Been Made Successfully")
                else:
                    print("Record You are Trying to Modify doesnt exist")
            elif (cch == 5):
                cursor.close()
                print("Exit")
                break
            else:
                print("Invalid Input")
                continue
        except ValueError:
            print("Invalid Input")
            continue




# import mysql.connector
# connectionn=mysql.connector.connect(host="localhost", user="root", passwd="alok",database="hms")
# create_tables(connectionn)
# rooms(connectionn)
