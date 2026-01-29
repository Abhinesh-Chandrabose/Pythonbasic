def add_item(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("Your cart is empty")
    elif(total<0):
        print("Invalid total amount")
    else:
        print("Total is $",total)
 
items = add_item("apple")
item= add_item("banana")
total = 0
for i in items:
    total+=5
checkout(total)