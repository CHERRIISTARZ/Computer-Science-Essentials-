#1st National Bank of Browntown Online Banking Application


class Customer(): #create an object named Customer
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00): #create name and balance, the balance starting with 100
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    def withdraw(self,amount): #create the function withdraw
    #add the ability to withdraw
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount): #create the function deposit
    #Add the ability to deposit
        self.balance = self.balance + amount
        return self.balance
    def checkBalance(self): #create the function checkBalance
    #Add the ability to check balance
        self.balance = self.balance
        return self.balance
print("Welcome to the 1st National Bank of Browntown App")
#explan what the app does
print("All new customers get $100 deposited into their account for signing up!")
print()
#ask the user what their name is
#create name variable
name = input("Let's Get Started! What is your name: ")
#create customer variable
customer = Customer(name)

#create a loop asking what the user would like to do
while True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance    (4) Quit")
    choice = input("->")

    #Withdraw
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        #Add a line that tells them their balance...after you have implemented balance check above

    #Add the ability to deposit
    if choice == "2":
        print("How much are you depositing?")
        amount = float(input("->"))
        customer.deposit(amount)
        print("You have deposited ", amount)

    #Add the ability to check balance
    if choice == "3":
        balance = customer.balance
        print("Your balance is", balance)

    #add the ability to quit, and break loop
    if choice == "4":
        break
#print a goodbye message
print("Thank you for using the 1st National Bank of Browntown App")