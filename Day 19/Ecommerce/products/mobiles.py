mobile_stock = 1
def buy_mobile():
    if mobile_stock>0:
        print("Thank you for purchase")
        mobile_stock -= 1
    else:
        print("out of stock")