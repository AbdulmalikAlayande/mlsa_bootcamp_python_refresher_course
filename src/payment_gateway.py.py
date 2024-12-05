# payment Gateway

class PaymentGateway:

    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount


    def paymentmethod(self):
        a=input('choose one of the following option \n credit card :press 1 \n paypal :press 2 \n crypto :press 3')

     

class CreditCardPayment(PaymentGateway):

    def __init__(self,currency,amount,card_number,cardholder_name,expiry_date):
        super(CreditCardPayment,self).__init__(currency,amount)
        self.card_number=card_number
        self.cardholder_name=cardholder_name
        self.expiry_date=expiry_date




    def paymentmethod(self):
        try:
            if len(str(self.card_number))==10:
                print("you details are valid")
            else:
                
                print("invalid card number")
                

        except:

            print("whoops an error occurred")

    def __str__(self):
            return self.cardholder_name



class PayPalPayment(PaymentGateway):

    def __init__(self,currency,amount,email):
        super(PayPalPayment,self).__init__(currency,amount)
        self.email=email




    def paymentmethod(self):

        try:
            if "@" in self.email and self.email[-3:]=="com":
                print("you email is valid")
            else:
                print("invalid email")
                

        except:
            print("whoops an error occurred")


    def __str__(self):
            return self.email

class CryptocurrencyPayment(PaymentGateway):

    def __init__(self,currency,amount,wallet_address,crypto_type):
        super(CryptocurrencyPayment,self).__init__(currency,amount)
        self.wallet_address=wallet_address
        self.crypto_type=crypto_type




    def paymentmethod(self):

        try:
            if len(self.wallet_address)==42:
                print("you wallet is valid")
            else:
                print("invalid walet address")
                

        except:
            print("whoops an error occurred")




    def __str__(self):
        return self.wallet_address





card=CreditCardPayment("Naira",100000,9137653841,"Adetunji Daniel","15/05/25")

paypal=PayPalPayment("Naira",100000,"adetunjidaniel2003@gmail.com")

   
crypto=CryptocurrencyPayment("Naira",100000,"0xdB055877e6c13b6A6B25aBcAA29B393777dD0a73","usdt")

                             
list1=[card,paypal,crypto]


for element in list1:
    element.paymentmethod()
    str(element)
    
  
                             




            

    
