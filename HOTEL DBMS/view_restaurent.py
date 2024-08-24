from search_customer import *
def view_rest():
    import class_cid
    myConnection = class_cid.connection#importing mysql credentials from class_cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid=class_cid.cid0
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
