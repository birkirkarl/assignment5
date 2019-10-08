import time
start = time.time()


def money_eater():
    global wallet
    money_dict={'n': 0.05, 'd': 0.10, 'q': 0.25, 'D': 1.00}
    try:
        money=input()
        money=money_dict[money]
        wallet += money
        return wallet
    except:
        print('\'{}\' is not a valid coin.'.format(money))

def machine_screen():
    global wallet
    print("A packet of candy costs $ 1.50. You have inserted $ {:.2f}.\nPlease insert coins:".format(wallet))
    print("\tn - Nickel\n\td - Dime\n\tq - Quarter\n\tD - Dollar")

wallet = 0
no_candy= True
while no_candy:
    machine_screen()
    money_eater()
    if wallet >= 1.5:
        wallet -=1.5
        print('Enjoy your candies. Your change is $ {:.2f}. Please visit again.'.format(wallet))
        no_candy = False
    

print(time.time()-start)