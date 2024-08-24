from search_customer import *
def view_fashion():
    import class_cid
    myConnection = class_cid.connection#importing mysql credentials from class_cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid=class_cid.cid0
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