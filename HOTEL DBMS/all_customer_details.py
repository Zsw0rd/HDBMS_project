from mysql.connector import *
def all_cus_det():
    import class_cid
    try:
        myConnection = class_cid.connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM C_DETAILS"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("CID=", rows[0], ",NAME=", rows[1], ",Address=", rows[2], ",AGE=", rows[3], ",Country=", rows[4],
                      ",PHONE no=", rows[5], ",Email=", rows[6], "\n")
        cursor.close()
    except Error as e:
        print("an error has occured")