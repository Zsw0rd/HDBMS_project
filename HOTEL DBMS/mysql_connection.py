#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection():
    import mysql.connector
    import class_cid
    myConnection=class_cid.connection
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()
