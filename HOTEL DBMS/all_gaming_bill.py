from mysql.connector import *
def allgame_bill():
    import mysql.connector
    import class_cid
    try:
        myConnection= class_cid.connection
        cursor=myConnection.cursor()
        sql = "SELECT * FROM GAMING"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("ORDERNO.=", rows[0], ",CID=", rows[1], ",GAMES=", rows[3], ",HOURS=", rows[4], ",BILL=", rows[5], "\n")
        cursor.close()
    except Error as e:
        print("an error has occured")