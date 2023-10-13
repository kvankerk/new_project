#!/usr/bin/env python
# coding: utf-8

# In[2]:


#BankAccount Assignment (kvankerk)


class BankAccount(object):
    def __init__(self, name, accountNumber, accountType, balance):
        self.name = name
        self.accountType = accountType
        self.balance = 0.0
        self.accountNumber = accountNumber
        self.deposit_list = []
        self.withdraw_list = []
        
    def deposit(self, amount):
        self.balance += amount
        self.deposit_list.append(amount)
        print (f"${amount} has been deposited")    
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdraw_list.append(amount)
            print (f"${amount} has been withdrawn")
        else:
            print ("You have insufficient funds for withdrawal.")
            
    def funds(self):
        print ("Available Balance: $", self.balance)
        
    def print_account_holder(self):
        print ("Name: ", self.name)
        print ("Account Number: ", self.accountNumber)
        print ("Account type (chequing or saving): ", self.accountType)
        print ("Starting Balance: $", self.balance)
        
    def file(self):
        #setting filename
        self.filename=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        print ("\n", self.filename)
    
    def transaction_history(self):
        print("Deposits: ", self.deposit_list)
        print("Withdrawals: ", self.withdraw_list)
        print("-------------------------------------------")
        

#input sample of customers

account1 = BankAccount("Sally Smith", 7491, "Saving" , 0) 
account2 = BankAccount("John Doe", 5209, "Chequing", 0)
account3 = BankAccount("Millie Moo", 2010, "Chequing", 0)

#print account holder details

account1.print_account_holder()
account1.deposit(575)
account1.deposit(1000)
account1.withdraw(200)
account1.deposit(250.67)
account1.funds()
account1.file()
account1.transaction_history()

print ("\n")

account2.print_account_holder()
account2.deposit(1000)
account2.withdraw(200)
account2.deposit(400)
account2.withdraw(2000)
account2.funds()
account2.file()
account2.transaction_history()

print ("\n")

account3.print_account_holder()
account3.deposit(15.75)
account3.withdraw(300)
account3.deposit(4000)
account3.deposit(2000)
account3.withdraw(16.79)
account3.funds()
account3.file()
account3.transaction_history()


# In[ ]:




