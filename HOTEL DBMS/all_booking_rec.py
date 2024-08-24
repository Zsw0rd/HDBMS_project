from mysql.connector import *
import class_cid
def all_bk():
    try:
        myConnection = class_cid.connection
        cursor = myConnection.cursor()
        sql = "SELECT * FROM ROOM_RENT"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("record is empty")
        else:
            for rows in data:
                print("CID=", rows[0], ",CHECKIN DATE=", rows[1], ",CHECKOUT DATE=",rows[2],",ROOM QUALITY=",rows[3],
                      ",NO OF DAYS=",rows[5],",Room NO=",rows[6],",Room Rent=",rows[7],"\n")
        cursor.close()
    except Exception as e:
        print("an error has occured",)
