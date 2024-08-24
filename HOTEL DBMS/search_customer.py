def searchCustomer():
    import class_cid
    myConnection = class_cid.connection
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("ENTER CUSTOMER ID : ")
        class_cid.cid0=cid
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