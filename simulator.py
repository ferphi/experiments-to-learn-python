import random
import string
numbers=string.digits
# We create a class to package the data and functions to be used:
class Stock_Market:
    #__init__ method in Python is used to initialize objects of a class. It is also called a constructor.
    def __init__(self):
        self.stocks = {"APPLE": random.randint(100,200), "GOOGLE": random.randint(10,100), "AMAZON": random.randint(50,150)}
        self.wallet = 1000
        self.portfolio = {}
    #show function
    def show(self):
        d=self.stocks
        print(f"\nCompany available: APPLE, price per action: {round(d.get('APPLE'),3)} $")
        print(f"Company available: GOOLE, price per action: {round(d.get('GOOGLE'),3)} $") 
        print(f"Company available: AMAZON, price per action: {round(d.get('AMAZON'),3)} $")           
    #purchase function
    def buy_stock(self, stock, amount):
        if stock in self.stocks:
            price=self.stocks[stock]
            total_cost=price*amount
            #updating the portfolio
            if stock in self.portfolio:
                self.portfolio[stock]+=amount
            else:
                self.portfolio[stock]=amount
            #verify that the available balance is sufficient to make the purchase and update said balance    
            if total_cost<=self.wallet:
                self.wallet-=total_cost
                print(f"Bought {amount} shares of {stock} for {total_cost}$")
            else:
                print("Insufficient funds to purchase this stock.")
        else:
            print("Stock not found")
    #sales function
    def sell_stock(self, stock, amount):
        #verifying what stock is in the portfolio
        if stock in self.portfolio:
            #verifying that you have the correct number of shares
            if amount<=self.portfolio[stock]:
                price=self.stocks[stock]
                total_income=price*amount
                self.wallet+=total_income
                self.portfolio[stock]-=amount
                print(f"Sold {amount} shares of {stock} for {total_income}$")
                if self.portfolio[stock]==0:
                    del self.portfolio[stock] #Removes the key:value pair. If the key does not exist, the KeyError exception is thrown.
            else:
                print("You don't have enough shares to sell")
        else:
            print("Stock not found in portfolio")
    #portfolio function
    def show_portfolio(self):
        print("\nPortfolio:")
        for stock, amount in self.portfolio.items():
            value=self.stocks[stock]*amount
            print(f"{stock}: {amount} shares, value: {round(value,3)}$")
    #wallet function
    def show_wallet(self):
        print(f"Available balance in your Wallet: {self.wallet}$")
    #function update
    def update_stock_prices(self):
        for stock in self.stocks:
            change=round(random.uniform(-50, 50),3) #price fluctuation
            self.stocks[stock]+=change

market=Stock_Market() #assigning the class

while True:
    #Option menu:
    print("\n1. Buy Stock")
    print("2. Sell Stock")
    print("3. Show Portfolio")
    print("4. Show Wallet")
    print("5. Exit")
    #Select your option
    option=input("\nEnter your option: ")
    #option 1 or 2:
    if option=="1" or option=="2":
        print(market.show())
        stock=input("\nWrite the name of the company you want to choose:")
        stock=stock.strip()
        stock=stock.upper()
        amount=input("\nEnter the amount to buy or sell as the case may be:")
        amount=amount.strip()
        #validation
        if all(x in numbers for x in amount):
            amount=int(amount)
            if option=="1":
                market.buy_stock(stock, amount)
            else:
                market.sell_stock(stock, amount)
        else:
            print("You did not enter a correct amount, please try again.")           
    #option 3:
    elif option=="3":
        market.show_portfolio()
    #option 4:
    elif option=="4":
        market.show_wallet()
    #option 5:
    elif option=="5":
        break
    #You did not select a correct option:
    else:
        print("\nYOU DID NOT ENTER A VALID OPTION, PLEASE TRY AGAIN!")
    market.update_stock_prices()
