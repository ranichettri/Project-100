class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.card = cardNumber
        self.pin = pinNumber

    def CashWithdrawl(self):
        print("Your cash is withdrawed in ****atm")

    def BalanceEnquiryl(self):
        print("Your balance is ******!!! ENJOY THE WEEKEND:)!")

    def CashDeposite(self):
        print("Your cash is deposited successful !!!")

user1 = Atm(23455,234568)
user1.BalanceEnquiryl()
user1.CashDeposite()