import mysql.connector
from datetime import datetime
from funtions_impt import *
myConnnection = ""
cursor = ""
print("#"*48)
print("#"*20, "HOTEL DATABASE MANAGEMENT SYSTEM", "#"*20)
User = input("Enter Username")
passwr = input("Enter password")

try:
    myConnection = mysql.connector.connect(host="localhost", user=User, passwd=passwr)
    if myConnection:
        print("\nYOUR CONNECTION To HOTELS DATABASE SYSTEM HAS BEEN ESTABLISHED !")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        # Importing all files so that we can use its functions functions
        from funtions_impt import *
        myConnection = mysql.connector.connect(host="localhost", user=User, passwd=passwr, database="HMS")
        create_tables(myConnection)
        if myConnection:
            MYSQLconnection(myConnection)
        while True:
            print("""
            
                1--->To Enter Customer Details
                2--->To Access/Edit Restaurant ROOM Details
                3--->To Enter CheckIN,CheckOUT Details and Customer's Room Details,Cost 
                4--->To View Customer's CheckIN and CheckOUT Details
                5--->To Access/Edit Restaurant FOOD Menu Details
                6--->To Enter Customer's Restaurant Bill
                7--->To View Customer's Restaurant Bill
                8--->To Enter Customer's Gaming Bill
                9--->To View Customer's Gaming Bill
                10--->To Enter Customer's Fashion store Bill
                11--->To View Customer's Fashion Bill
                12--->To Display Customer's Details
                13--->To Generate Customer's Total Bill And Display It
                14--->To Generate Customer's Old Bill And Display It
                15--->To Display All Customers Records 
                16--->To Display All Customers CheckIN,CheckOUT Details and RoomRent Details
                17--->To Display All Customers  Restaurant Bills
                18--->To Display All Customers Gaming Bills
                19--->To Display All Customers Fashion store Bills
                20--->>To Display All Customers Total Bills
                21--->>To Update Or Delete Records
                22--->>EXIT PROGRAM
                """)
            # user choice which will choose one of the functions
            try:
                choice = int(input("Enter Your Choice:"))
                if choice == 1:
                    userEntry(myConnection)   # user_entry.py
                elif choice == 2:
                    rooms(myConnection)
                elif choice == 3:
                    roomRent(myConnection)    # roomRent.py
                elif choice == 4:
                    view_inout(myConnection)  # view_inout.py
                elif choice == 5:
                    food(myConnection)
                elif choice == 6:
                    Restaurent(myConnection)  # restaurant.py
                elif choice == 7:
                    view_rest(myConnection)   # view_restaurent.py
                elif choice == 8:
                    Gaming(myConnection)      # gaming.py
                elif choice == 9:
                    view_gaming(myConnection)  # view_gaming.py
                elif choice == 10:
                    Fashion(myConnection)     # cloth_store.py
                elif choice == 11:
                    view_fashion(myConnection)  # view_fashion.py
                elif choice == 12:
                    searchCustomer(myConnection)  # search_customer.py
                elif choice == 13:
                    totalAmount(myConnection)  # total_amount.p

                elif choice == 14:
                    searchOldBill(myConnection)  # old_bill.py
                elif choice == 15:
                    all_cus_det(myConnection)  # all_customer_details.py
                elif choice == 16:
                    all_bk(myConnection)       # all_booking_record.py
                elif choice == 17:
                    all_restbill_det(myConnection)  # all_restbill_details.py
                elif choice == 18:
                    allgame_bill(myConnection)  # all_gaming_bill.py
                elif choice == 19:
                    all_fasbill(myConnection)  # all_fashionbills.py
                elif choice == 20:
                    alltotbill(myConnection)  # all_totalbill.py
                elif choice == 21:
                    print("Unable to access this at this time,work in progress")
                    #altdel_rec(myConnection)#altdel.py
                elif choice == 22:
                    print("Exiting.......")
                    break
                    #program breaks out of loop and exits the program
                else:
                    print("Invalid Input, Please Try Again !!! ")
            except ValueError:
                print("Invalid Input, Please Try Again !!! ")
except Exception as e:
    print(e)
    print("Error Establishing connection to SQL server!")
    print("Incorrect Username or Password!")

