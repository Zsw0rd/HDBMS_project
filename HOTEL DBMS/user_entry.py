def userEntry():
    import class_cid
    myConnection = class_cid.connection#importing mysql credentials from class_cid
    if myConnection:
        while True:
            cursor=myConnection.cursor()
            cid = input("Please Enter Customer Identification Number : ")
            sql0="SELECT CID FROM C_DETAILS WHERE CID=%s"#1Checking if The CID already exists to avoid duplication/errors
            cursor.execute(sql0,(cid,))
            data=cursor.fetchall()
            try:        #using try and except method to check if any data is present in the tables
                b=data[0][0]
            except IndexError:
                b=['null']
            if cid==b:
                print("This CID Already Exists")
                #2Checking if The CID already exists to avoid duplication/errors using if/else
            else:
                #all user inputing customer details
                name = input("Enter Customer Name : ")
                address = input("Enter Customer Address : ")
                age= input("Enter Customer Age : ")
                nationality = input("Enter Customer Country : ")
                phoneno= input("Enter Customer Contact Number : ")
                email = input("Enter Customer Email : ")
                sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"#place holder for variables
                values= (cid,name,address,age,nationality,phoneno,email)#storing all user inputs in a single variable
                cursor.execute(sql,values)#executing the place holder and the values
                cursor.execute("COMMIT")#commiting the statement so that all values will be stored in database
                print("\nNew Customer Entered In The System Successfully !")
                cursor.close()
                return False
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")