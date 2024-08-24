from search_customer import *
def Gaming():
 import class_cid
 myConnection = class_cid.connection
 customer=searchCustomer()
 if customer:
  if myConnection:
   cursor=myConnection.cursor()
   sql01 = "SELECT CID FROM room_rent WHERE CID=%s"
   cid = class_cid.cid0
   cursor.execute(sql01, (cid,))
   p = cursor.fetchall()
   if not p:
    print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Gaming Arcade")
   else:
    q = p[0][0]
    if q!= class_cid.cid0:
     print("Please Fill Up CheckIn and CheckOUT details first before Accessing the Gaming Arcade")
    else:
     while True:
      order = input("Please Enter Order Number:")
      sql0 = "SELECT ORDER_NO FROM GAMING WHERE ORDER_NO=%s"
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
       ##### CMR HOTELS GAMING HUB #####
       1. Table Tennis -----> 150 Rs./HR
       2. Bowling -----> 100 Rs./HR
       3. Cart Racing -----> 250 Rs./HR
       4. VR Gaming -----> 400 Rs./HR
       5. Video Games -----> 300 Rs./HR
       6. Swimming Pool Games -----> 350 Rs./HR
       7. Exit
       """)
       try:
        gamechoice=int(input("Enter What Game The Customer wants To Play : "))
        try:
         hour=int(input("Enter No Of Hours The Customer wants To Play : "))
         print("\n\n#################################################")
         if gamechoice==1:
          print("The Customer Has SELECTED TO PLAY : Table Tennis")
          game='Table Tennis'
          gamingbill = hour * 150
         elif gamechoice==2:
          print("The Customer Has SELECTED TO PLAY : Bowling")
          game='Bowling'
          gamingbill = hour * 100
         elif gamechoice==3:
          print("The Customer Has SELECTED TO PLAY : Cart Racing")
          gamingbill = hour * 250
          game='Cart Racing'
         elif gamechoice==4:
          print("The Customer Has SELECTED TO PLAY : VR Gaming")
          game='VR Gaming'
          gamingbill = hour * 400
         elif gamechoice==5:
          print("The Customer Has SELECTED TO PLAY : Video Games")
          game='Video Games'
          gamingbill = hour * 300
         elif gamechoice ==6:
          print("The Customer Has SELECTED TO PLAY : Swimming Pool Games")
          game='Swimming Pool Games'
          gamingbill = hour * 350
         elif gamechoice==7:
          print('\nHope The Customer Vist Again')
          game='none'
          gamingbill = 0
         else:
          print("Invalid Input,Please Try Again")
          return
         cid = class_cid.cid0
         sql= "INSERT INTO GAMING VALUES(%s,%s,%s,%s,%s,%s)"
         values= (order,cid,gamechoice,game,hour,gamingbill)
         cursor.execute(sql,values)
         cursor.execute("COMMIT")
         sql2 = "SELECT GAMES,HOURS,GAMING_BILL FROM GAMING WHERE ORDER_NO= %s"
         cursor.execute(sql2, (order,))
         data1 = cursor.fetchall()
         a = data1[0][0]
         b = data1[0][1]
         c = data1[0][2]
         print("\n\n#################################################")
         print("Order details as in Below")
         print("Game=", a)
         print("Hours=", b)
         print("Bill=", c)
         print("Your Gaming Bill Is : Rs. ",gamingbill)
         print("\n *** WE HOPE The Customer WILL ENJOY The CustomerR GAME ***")
         print("\n\n#################################################")
         cursor.close()
        except ValueError:
         print("Invalid Input,Please Try Again")
       except ValueError:
        print("Invalid Input,Please Try Again")
       return False
  else:
   print("ERROR ESTABLISHING MYSQL CONNECTION !")