# importing mysql
import mysql.connector
myConnnection = ""
cursor = ""
print("#"*48)
print("#"*10,"CMR HOTELS DATABASE SYSTEM","#"*10)
userName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")
if userName=='root' and password=='#Your System Password':
    myConnection=mysql.connector.connect(host="localhost",user="root",passwd="#YOUR SQL PASSWORD")
    if myConnection:
        print("\nYOUR CONNECTION To CMR HOTELS DATABASE SYSTEM HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        #Importing all files so that we can us-`    e its functions functions
        from create_table import *
        create_tables()
        from all_customer_details import *
        from all_restbill_details import *
        from all_gaming_bill import *
        from all_fashionbills import *
        from all_totalbill import *
        from cloth_store import *
        from mysql_connection import *
        from old_bill import *
        from restaurant import *
        from roomRent import *
        from user_entry import *
        from total_amount import *
        from gaming import *
        from all_booking_rec import *
        from altdel import *
        from view_restaurent import *
        from view_gaming import *
        from view_fashion import *
        from view_inout import *
        if myConnection:
            MYSQLconnection()
        while True:
            print("""
                1--->To Enter Customer Details
                2--->To Enter CheckIN,CheckOUT Details and Customer's Room Details,Cost 
                3--->To View Customer's CheckIN and CheckOUT Details
                4--->To Enter Customer's Restaurent Bill
                5--->To View Customer's Restaurent Bill
                6--->To Enter Customer's Gaming Bill
                7--->To View Customer's Gaming Bill
                8--->To Enter Customer's Fashion store Bill
                9--->To View Customer's Fashion Bill
                10--->To Display Customer's Details
                11--->To Generate Customer's Total Bill And Display It
                12--->To Generate Customer's Old Bill And Display It
                13--->To Display All Customers Records 
                14--->To Display All Customers CheckIN,CheckOUT Details and RoomRent Details
                15--->To Display All Customers  Restaurent Bills
                16--->To Display All Customers Gaming Bills
                17--->To Display All Customers Fashion store Bills
                18--->>To Display All Customers Total Bills
                19--->>To Update Or Delete Records
                20--->>EXIT PROGRAM
                """)
            #user choice which will choose one of the functions
            try:
                choice = int(input("Enter Your Choice:"))
                if choice == 1:
                    userEntry()   #user_entry.py
                elif choice == 2:
                    roomRent()    #roomRent.py
                elif choice == 3:
                    view_inout()  #view_inout.py
                elif choice == 4:
                    Restaurent()  #restaurant.py
                elif choice == 5:
                    view_rest()   #view_restaurent.py
                elif choice == 6:
                    Gaming()      #gaming.py
                elif choice == 7:
                    view_gaming() #view_gaming.py
                elif choice == 8:
                    Fashion()     #cloth_store.py
                elif choice == 9:
                    view_fashion()#view_fashion.py
                elif choice == 10:
                    searchCustomer()#search_customer.py
                elif choice == 11:
                    totalAmount() #total_amount.py
                    print("""\nIf You Think something is wrong in this table or any other table
                          it is recommended to delete this record and make alteration to the any other record
                          before trying again to calculate Total customer's bill""")
                elif choice == 12:
                    searchOldBill()#old_bill.py
                elif choice == 13:
                    all_cus_det()  #all_customer_details.py
                elif choice == 14:
                    all_bk()       #all_booking_record.py
                elif choice == 15:
                    all_restbill_det()#all_restbill_details.py
                elif choice == 16:
                    allgame_bill()#all_gaming_bill.py
                elif choice == 17:
                    all_fasbill()#all_fashionbills.py
                elif choice == 18:
                    alltotbill()#all_totalbill.py
                elif choice == 19:
                    altdel_rec()#altdel.py
                elif choice== 20:
                    print("Exiting.......")
                    break
                    #program breaks out of loop and exits the program
                else:
                    print("Invalid Input, Please Try Again !!! ")
            except ValueError:
                print("Invalid Input, Please Try Again !!! ")
else:
    #if the user enters an incorrect user id or password,the application needs to be restarted
    print("Username or password is incorrect")
    print("Please restart the application")
