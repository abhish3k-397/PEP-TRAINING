laptop_stock = 1
def buy_laptop():
    if laptop_stock>0:
        print("Thank you for purchasing laptop")
        laptop_stock -= 1
    else:
        print("out of stock")
