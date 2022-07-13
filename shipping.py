def main():
    shipweight=float(input('Please enter the weight of the item you wish to ship: '))
    shipping_charges(shipweight)
def shipping_charges(shipweight):
    if shipweight <= 2:
        print(shipweight,"pounds will cost you $1.50 per pound.")
        rate1=1.50
        total= rate1 * shipweight
        print("Therefore, your total shipping charge would be " )
    elif shipweight <= 6:
        print(shipweight,"pounds will cost you $3.00 per pound.")
        rate2=3.00
        total= rate2 * shipweight
        print("Therefore, your total shipping charge would be" )
    elif shipweight <= 10:
        print(shipweight,"pounds will cost you $4.00 per pound.")
        rate3=4.00
        total= rate3 * shipweight
        print("Therefore, your total shipping charge would be" )
    elif shipweight > 10:
        print(shipweight,"pounds will cost you $4.75 per pound.")
        rate4=4.75
        total= rate4 * shipweight
        print("Therefore, your total shipping charge would be")
main()
