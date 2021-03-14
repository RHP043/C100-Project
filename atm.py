class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin=pin
    def check_balance(self):
        print("yoir balance is 67890")
    def withdrawl(self,amount):
        new_amount=67890  -amount
        print("our remaining money is: "+str(new_amount))

def main():
    card_number=input("instert your card number: ")
    pin_number=input("enter your pin number: ")

    new_user=Atm(card_number,pin_number)
    print("choose your activivty")
    print("1.balanace enquiry 2. withdrawl")
    activity=int(input("enter actvity number: "))

    if(activity==1):
        new_user.check_balance()
    elif (activity==2):
        amount=int(input("amount: "))

        new_user.withdrawl(amount)
    else:
        print("enter a valid number")

if __name__=="__main__":
    main()