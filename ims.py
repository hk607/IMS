# -*- coding: utf-8 -*-
"""IMS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19zgu5tJ5doKjil-gX1AWwyVhXizB7lio
"""

import json




while(1):
    print("\tINVENTORY MANAGEMENT SYSTEM")
    print("\tMENU")
    print("\n\t1.To  view the Items  Available at store")
    print("\t2.To add more items in the store")
    print("\t3.Puchase any Products")
    print("\t4.View Sales of the Products")
    print("\t5.Exit")
    choice = int(input("Enter  Choice : "))

    
    if(choice == 1):
      fd = open("record.json",'r')
      r = fd.read()
      fd.close()
      record = json.loads(r)
      print("welcome  to  the store Items  Available at store")
      print(record)





    elif(choice == 2):
      print("To add more items in the store")
      prod_id = str(input("Enter product id:"))
      name = str(input("Enter name:"))
      price = int(input("Enter price:"))
      quantity = int(input("Enter quantity:"))
      manufacturing_date = str(input("Enter  manufacturing_date:"))
      expiry_date = str(input("Enter  expiry_date:"))

      record[prod_id] = {'name': name, 'price': price, 'quantity': quantity}
      js = json.dumps(record)
      fd = open("record.json",'w')
      fd.write(js)
      fd.close()
      
    elif(choice == 3):
      print("Puchase any Products")
      #sold_item=0
      #while ():
      ui_prod  = str(input("Enter the Item id from the list shown above: "))
      ui_quant = int(input("Enter the quantity  you want to purchase: "))
      if (ui_prod != prod_id  or  ui_quant>quantity):
        print("Item is not available")
      else:
        print("Item available")
        print("Product: ", record[ui_prod]['name'])
        print("Price: ", record[ui_prod]['price'])
        print("Billing Amount: ", record[ui_prod]['price'] * ui_quant)
        print("Thanks_for_shopping_visit_again")
        #To Change the record in the database
        record[ui_prod]['quantity'] = records[ui_prod]['quantity'] - ui_quant

    elif(choice == 4):
      file = open("sales.json", 'r')
      data = file.read()
      record = json.loads(data)
      print("SOLD PRODUCT LIST")
      print("Product Id:", "Product Name:", "Price:", "Quantity:")
      for i in record.keys():
        print(i, record[i]['name'], record[i]['price'])
      file.close()
    elif(choice == 5):

        print("\n\tStore Exited !!")
        break

    else:
        print("Invalid Choice!!")

    var = input("\n\t\tPress 0 to return to menu : ")
