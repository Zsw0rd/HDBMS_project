from search_customer import searchCustomer
def totalAmount():
    import class_cid
    customer=searchCustomer()
    if customer:
        myConnection = class_cid.connection
        if myConnection:
            cursor=myConnection.cursor()
            sql01 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
            cid = class_cid.cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Total Bill Section")
            else:
                q = p[0][0]
                if q != class_cid.cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Total Bill Section")
                else:
                    sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    cid=class_cid.cid0
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
                        cid2=class_cid.cid0
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