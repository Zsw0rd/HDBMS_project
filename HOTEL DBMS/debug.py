cid0=''
from datetime import datetime
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