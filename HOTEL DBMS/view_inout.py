from search_customer import *
def view_inout():
    import class_cid
    myConnection = class_cid.connection#importing mysql credentials from class_cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = class_cid.cid0
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
                          rows[3], ",NO OF DAYS=", rows[5],",Room NO=", rows[6], ",Room Rent=", rows[7], "\n")
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
