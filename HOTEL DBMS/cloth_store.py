from search_customer import *
def Fashion():
    import class_cid
    myConnection = class_cid.connection
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql01 = "SELECT CID FROM ROOM_RENT WHERE CID=%s"
            cid = class_cid.cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Fashion store")
            else:
                q = p[0][0]
                if q != class_cid.cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Fashion store")
                else:
                    while True:
                        order = input("Please Enter Order no: ")
                        sql0 = "SELECT CID FROM FASHION WHERE ORDER_NO=%s"
                        cursor.execute(sql0, (order,))
                        x = cursor.fetchall()
                        try:
                            y = x[0][0]
                        except IndexError:
                            y = ['null']
                        if order == y:
                            print("OrderNO. Already Exists")
                            continue
                        else:
                            print("""
                            ##### CMR HOTELS FASHION STORE #####
                            1.Shirts - ----> 1500Rs.
                            2.T - Shirts - ----> 300Rs.
                            3.Pants - ----> 2000Rs.
                            4.Jeans - ----> 4000Rs.
                            5.Tassel top - ----> 500Rs.
                            6.Gown - ----> 3000Rs.
                            7.Western dress - ----> 3000Rs.
                            8.Skirts - ----> 400Rs.
                            9.Trousers - ----> 200Rs.
                            10.InnerWear - ----> 30Rs.
                            11.Not Interested
                            """)
                            try:
                                dresschoice=int(input("Please Enter The Customer's Choice: "))
                                try:
                                    quantity=int(input("Please Enter The Quantity: "))
                                    if type(quantity)==int:
                                        if dresschoice==1:
                                            print("\nThe Customer Has purchased -----> Shirts")
                                            dress = 'Shirts'
                                            fashionbill = quantity * 1500
                                        elif dresschoice==2:
                                            print("\nThe Customer Has purchased -----> T-Shirts")
                                            dress = 'T-Shirts'
                                            fashionbill = quantity * 300
                                        elif dresschoice==3:
                                            print("\nThe Customer Has purchased -----> Pants")
                                            dress = 'Pants'
                                            fashionbill = quantity * 2000
                                        elif dresschoice==4:
                                            print("\nThe Customer Has purchased -----> Jeans")
                                            dress = 'Jeans'
                                            fashionbill = quantity * 4000
                                        elif dresschoice==5:
                                            print("\nThe Customer Has purchased -----> Tassel top")
                                            dress = 'Tassel top'
                                            fashionbill = quantity * 500
                                        elif dresschoice==6:
                                            print("\nThe Customer Has purchased -----> Gown")
                                            dress = 'Gown'
                                            fashionbill = quantity * 3000
                                        elif dresschoice==7:
                                            print("\nThe Customer Has purchased -----> Western dress")
                                            dress = 'Western dress'
                                            fashionbill = quantity * 3000
                                        elif dresschoice==8:
                                            print("\nThe Customer Has purchased -----> Skirts")
                                            dress = 'Skirts'
                                            fashionbill = quantity * 400
                                        elif dresschoice==9:
                                            print("\nThe Customer Has purchased -----> Trousers")
                                            dress = 'Trousers'
                                            fashionbill = quantity * 200
                                        elif dresschoice==10:
                                            print("\nThe Customer Has purchased -----> InnerWear")
                                            dress = 'InnerWear'
                                            fashionbill = quantity * 30
                                        elif dresschoice==11:
                                            print("\nHope You Find Something better next Time , Please Visit Again")
                                            dress = 'none'
                                            fashionbill = quantity * 0
                                        else:
                                            print("Invalid Input, Please Try Again")
                                            return
                                        sql = "INSERT INTO FASHION VALUES(%s,%s,%s,%s,%s,%s)"
                                        cid = class_cid.cid0
                                        values = (order, cid, dresschoice, dress, quantity, fashionbill)
                                        cursor.execute(sql, values)
                                        cursor.execute("COMMIT")
                                        sql2 = "SELECT DRESS,AMOUNT,BILL FROM FASHION WHERE ORDER_NO= %s"
                                        cursor.execute(sql2, (order,))
                                        data = cursor.fetchall()
                                        a = data[0][0]
                                        b = data[0][1]
                                        c = data[0][2]
                                        print("\n\n#################################################")
                                        print("Order details as in Below")
                                        print("Dress=", a)
                                        print("Quantity=", b)
                                        print("Bill=", c)
                                        print("\nYour Total Clothing Bill Is : ", fashionbill)
                                        print("\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!")
                                        print("\n\n#################################################")
                                        cursor.close()
                                except ValueError:
                                    print('Invalid Input,Please Try Again')
                            except ValueError:
                                print('Invalid Input,Please Try Again')
                            return False
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")