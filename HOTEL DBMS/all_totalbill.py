from mysql.connector import *
def alltotbill():
    import mysql.connector
    import class_cid
    try:
        myConnection = class_cid.connection
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
    except Error as e:
        print("an error has occured")