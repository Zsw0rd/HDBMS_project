from mysql.connector import *
def all_restbill_det():
    import class_cid
    try:
        myConnection = class_cid.connection
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
    except Error as e:
        print("an error has occured")