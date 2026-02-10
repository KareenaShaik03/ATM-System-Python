 class ATM:
    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.menu()

    def menu(self):
        while True:
            print("""
========== ATM MENU ==========
1. Generate PIN
2. Deposit Money
3. Withdraw Money
4. Balance Check
5. Exit
==============================
""")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                self.create_pin()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.balance_check()
            elif choice == 5:
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

    def create_pin(self):
        self.__pin = input("Set your 4-digit PIN: ")
        print("PIN generated successfully.")

    def authenticate(self):
        if self.__pin is None:
            print("Please generate a PIN first.")
            return False

        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            return True
        else:
            print("Invalid PIN.")
            return False

    def deposit(self):
        if self.authenticate():
            try:
                amount = int(input("Enter deposit amount: "))
                if amount > 0:
                    self.__balance += amount
                    print("Deposit successful.")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount.")

    def withdraw(self):
        if self.authenticate():
            try:
                amount = int(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > self.__balance:
                    print("Insufficient balance.")
                else:
                    self.__balance -= amount
                    print("Withdrawal successful.")
            except ValueError:
                print("Invalid amount.")

    def balance_check(self):
        if self.authenticate():
            print(f"Current Balance: ₹{self.__balance}")


# Run ATM
atm = ATM()
