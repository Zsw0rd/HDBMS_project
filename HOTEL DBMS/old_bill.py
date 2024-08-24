from search_customer import *
def searchOldBill():
    import class_cid
    myConnection =class_cid.connection
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            cid = class_cid.cid0
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
