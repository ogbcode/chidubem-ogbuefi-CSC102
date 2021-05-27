# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:14:46 2021

@author: SST Computer Lab
"""
import pandas
def customerbank():
    customernames=list[name]
    customeraccountbalance=list[accountB]
    customerpin=list[password]
    tab={"name":name,"account balance":customeraccountbalance,"pin":customerpin}
    customers_in_bank=pandas.DataFrame(tab)
    customers_in_bank
class XBank:
    loggedinCounter = 0
    def __init__(self,theatmpin,theaccountbalance,thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        XBank.loggedinCounter  = XBank.loggedinCounter + 1
    
    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print("Sorry we are not able to process at this time")
        else:
            print("Collect your cash....Thanks for banking with Xbank")
    def ChangePin(self, newpin):
    
        newpin=input("what do waant your new pin to be")
        self.atmpin = newpin
        print("Your Pin has been changed...Thanks for banking with Xbank")
    @classmethod  
    def NoOfCustomersLoggedin (cls):
        print("we have a total of" + str(cls.loggedinCounter) + " that have logged in")
        
        

f = open("C:\\Users\SST Computer Lab\Documents\database for bankin application.txt",'r')

print(f.readlines)
password = []
accountB = []
name = []
breaker =  []
for x in f:
   breaker = x.split(' ')
   password.append(breaker[0])
   accountB.append(breaker[1]) 
   name.append(breaker[2])
   break


print("enter your pin........")

pasw = input()

if(pasw ==password[0]):
    customer = XBank(password[0],accountB[0],name[0])
    print("your password is",password[0])
    print("your accountbalance is",accountB[0])
    print("your name is",name[0])
else:
    print("sorry your password does not match")

