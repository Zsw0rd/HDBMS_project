from search_customer import *


def Restaurent():
    import class_cid
    myConnection = class_cid.connection  # importing mysql credentials from class_cid
    customer = searchCustomer()
    quantity = 0
    dish = ''
    if customer:
        restaurentbill = 0
        if myConnection:
            cursor = myConnection.cursor()
            sql01 = "SELECT CID FROM room_rent WHERE CID=%s"
            cid = class_cid.cid0
            cursor.execute(sql01, (cid,))
            p = cursor.fetchall()
            if not p:
                print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Restaurent")
            else:
                q = p[0][0]
                if q != class_cid.cid0:
                    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Restaurent")
                else:
                    while True:
                        order = input("Please Enter Order Number:")
                        sql0 = "SELECT ORDER_NO FROM Restaurent WHERE ORDER_NO=%s"
                        # 1Checking if The order already exists to avoid duplication/errors
                        cursor.execute(sql0, (order,))
                        x = cursor.fetchall()
                        try:  # using try and except method to check if any data is present in the tables
                            y = x[0][0]
                        except IndexError:
                            y = ['null']
                        if order == y:
                            print("OrderNO. Already Exists")  # 2Checking if The order already exists to avoid duplication/errors using if/else
                            continue
                        else:
                            # printing various choices user can choose from
                            print('##### CMR HOTELS MENU #####')
                            print("1. Vegetarian Combo -----> 300 Rs.")
                            print("2. Non-Vegetarian Combo -----> 500 Rs.")
                            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
                            print("""4. Beverages below
                                1.Coffee-----> 200 Rs.
                                2.Tea-----> 150 Rs.
                                3.Black Coffee-----> 250 Rs.
                                4.Milk-----> 130 Rs.
                                5.Beer-----> 600 Rs.
                                6.Whisky-----> 650 Rs.""")
                            print("5. Not Interested ")
                            try:
                                choice_dish = int(input("Enter Customer's Cuisine/Beverages Choice: "))  # user input
                                if choice_dish == 1:  # if loop begins
                                    try:
                                        quantity = int(input("Enter Quantity : "))
                                        print("\nCustomer Has Chosen The ORDER: Vegetarian Combo ")
                                        dish = 'Vegetarian Combo'
                                        restaurentbill = quantity * 300
                                    except ValueError:
                                        print("Invalid Input,Please Try Again")
                                elif choice_dish == 2:
                                    try:
                                        quantity = int(input("Enter Quantity : "))
                                        print("\nCustomer Has Chosen The ORDER: Non-Vegetarian Combo ")
                                        dish = 'Non-Vegetarian Combo'
                                        restaurentbill = quantity * 500
                                    except ValueError:
                                        print("Invalid Input,Please Try Again")
                                elif choice_dish == 3:
                                    try:
                                        quantity = int(input("Enter Quantity : "))
                                        print("\nCustomer Has Chosen The ORDER: Vegetarian & Non-Vegetarian Combo ")
                                        dish = 'Veg & Non-Veg Combo'
                                        restaurentbill = quantity * 750
                                    except ValueError:
                                        print("Invalid Input,Please Try Again")
                                elif choice_dish == 4:
                                    print("\nEnter Customer's Beverage Choice")
                                    print("""
                                    1.Coffee-----> 200 Rs.
                                    2.Tea-----> 150 Rs.
                                    3.Black Coffee-----> 250 Rs.
                                    4.Milk-----> 130 Rs.
                                    5.Beer-----> 600 Rs.
                                    6.Whisky-----> 650 Rs.""")
                                    try:
                                        choice_dish1 = int(input("Enter Customer's Beverage Choice"))
                                        if choice_dish1 == 1:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Coffee ")
                                                dish = 'Coffee'
                                                restaurentbill = quantity * 200
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        elif choice_dish1 == 2:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Tea ")
                                                dish = 'Tea'
                                                restaurentbill = quantity * 150
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        elif choice_dish1 == 3:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Black Coffee ")
                                                dish = 'Black Coffee'
                                                restaurentbill = quantity * 250
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        elif choice_dish1 == 4:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Milk ")
                                                dish = 'Milk'
                                                restaurentbill = quantity * 130
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        elif choice_dish1 == 5:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Beer ")
                                                dish = 'Beer'
                                                restaurentbill = quantity * 600
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        elif choice_dish1 == 6:
                                            try:
                                                quantity = int(input("Enter Quantity : "))
                                                print("\nCustomer Has Chosen The ORDER: Whisky ")
                                                dish = 'Whisky'
                                                restaurentbill = quantity * 650
                                            except ValueError:
                                                print("Invalid Input,Please Try Again")
                                        else:
                                            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                                    except ValueError:
                                        print("Invalid Input,Please Try Again")
                                elif choice_dish == 5:
                                    print("\nHope You Vist Again")
                                    dish = 'none'
                                    restaurentbill = 0
                                else:
                                    print("Invalid Input,Please Try Again")
                                    return
                                cid = class_cid.cid0
                                # we are allowing multiple CID's in the table because one cid can have multiple orders
                                # ,hence here order no is unique
                                sql = "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s,%s,%s)"  # place holder for variables
                                values = (order, cid, choice_dish, dish, quantity, restaurentbill)
                                # storing all variables in a single variable
                                cursor.execute(sql, values)
                                cursor.execute("COMMIT")
                                sql2 = "SELECT CUISINE,QUANTITY,BILL FROM RESTAURENT WHERE ORDER_NO= %s"
                                cursor.execute(sql2, (order,))
                                data = cursor.fetchall()  # fetching cuisine,quantiity and bills
                                a = data[0][0]
                                # data[0][0] means its fetching a string from a list of tuples stored in variable data
                                b = data[0][1]
                                c = data[0][2]
                                print("\n\n#################################################")
                                print("Order details as in Below")
                                print("Cuisine=", a)
                                print("Quantity=", b)
                                print("Bill=", c)
                                print("Your Total Bill Amount Is : Rs. ", restaurentbill)
                                print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
                                print("\n\n#################################################")
                                cursor.close()
                            except ValueError:
                                print("Invalid Input,Please Try Again")
                            return False
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
