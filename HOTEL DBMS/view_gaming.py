from search_customer import *
def view_gaming():
    import class_cid
    myConnection = class_cid.connection#importing mysql credentials from class_cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = class_cid.cid0
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