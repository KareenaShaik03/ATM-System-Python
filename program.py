class Atm:
    def __init__(self):
        self.__pin =""
        self.__balance=0
        self.menu()
        
    def get_pin(self):
        return self.__pin
        
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("Pin changed")
            
    def menu(self):
        
        print("""Hello.........
                  1.Genetate pin 
                  2.Deposite  
                  3.withdraw 
                  4.Balance Check 
                  5.Exit""")
        user_input = int(input("Enter the option:"))
            
        if user_input =="1":
            self.create_pin()
        elif user_input =="2":
            self.deposite()
        elif user_input =="3":
            self.withdraw()
        elif user_input =="4":
            self.balance_check()
        elif user_input =="5":
            print("Exited")
            
    def create_pin(self):
        self.__pin = input("Enter Your pin")
        print("Pin Generated")
        
    def deposite(self):
        temp = int(input("Enter the pin"))
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance=self.__balance + amount
            print("Deposite sucessful")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        temp = int(input("Enter the pin"))
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance =self.__balance - amount
                print("Withdraw successful")
            else:
                print("Unsufficient amount")
        else:
            print("Invalid pin")
            
    def balance_check(self):
        temp = int(input("Enter the pin"))
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            print(self.__balance)
        else:
            print("Invalid Pin")
            
sbi =Atm()    