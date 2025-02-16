from datetime import datetime

Name=input("Enter your name: ")

print("Welcome to the ESS Supermarket, "+Name+"!")

#List of Items available in the Supermarket
lists='''
Rice                  Rs 20/kg
Sugar                 Rs 30/kg
Salt                  Rs 10/kg
oil(1ltr)             Rs 100
Paneer                Rs 110/kg
Maggi                 Rs 12/pack
Tea                   Rs 50/pack
Coffee                Rs 60/pack
Biscuits              Rs 10/pack 
Colgate Tooth Paste   Rs 20/pack
'''

#declaring variables
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[] #item list
qlist=[] #quantity list
plist=[] #price list

#Rates of Items
items={'Rice':20,'Sugar':30,'Salt':10,'oil':100,'Paneer':110,'Maggi':12,'Tea':50,'Coffee':60,'Biscuits':10,'Colgate Tooth Paste':20} #keys


option=int(input("Do you want to see the list of items available in the Supermarket? Press 1 for Yes and 2 for No: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If You Want to buy Press 1 or Press 2 to skip: ")) #if user wants to buy the item
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the item you want to buy: ")
        quantity=int(input("Enter the quantity : "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            Gst=(totalprice*5)/100
            finalprice=totalprice+Gst
        else:
            print("You Entered Item is not available")
    else:
        print("You Entered Invalid Number")
    inp=int(input("Can I Bill The Items 1 For Yes or 2 For No:")) #if user wants to buy more items   
    if inp==1:
        pass 
    if finalprice!=0:
        print(25*"=","ESS Supermarket",25*"=")
        print(28*" ","Pulivendula")
        print("Name:",Name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("s.no",8*" ","Items",8*" ","Quantity",8*" ","Price")
        for i in range(len(pricelist)):
            print("Item: ",5*' ',ilist[i],8*' ',qlist[i],15*' ',plist[i])
            print(75*"-")
            print(50*" ","Total Price: ",'Rs',totalprice)
            print(50*" ","GST: ",7*" ",'Rs',Gst)
            print(75*"-")
            print(50*" ","Final Amount: ",'Rs',finalprice)
            print(75*"-")
            print(25*'*',"Thank You Visit Again",25*'*')
            print(75*"-")





            
        