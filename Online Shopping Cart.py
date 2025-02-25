# Product List
Products={
    'SmartPhone':(699,'Electronics'),
    'T-Shirt': (25, "Clothing"),
    'Milk (1L)': (3, "Groceries"),
    'Vacuum Cleaner': (150, "Home"),
}
for items in Products:
        details=Products[items]
        print('Product :',items,'|','Price:',details[0],'|','Catogary:',details[1])
cart=[]
i=None
# User Choice
while i!='proceed':
    user_input=str(input("Select the item to add to the cart "))
    if user_input in Products :
        cart.append(user_input)
        print('item added to the cart')
    else:
        print("Item is not present in cart")
    next=str(input("Would you like to proceed further? tap yes otherwise no "))
    if next=='no' or next=='yes':
        if next=='no':
            i='proceed'
        else:
            pass
    else:
         print('Enter valid command')
print("Your Cart Items:",cart)
# Printing the Bill:
bill=0
for items in cart:
     bill+=Products[items][0]
print('Your total bill is',bill)
          
          
     
     

          









