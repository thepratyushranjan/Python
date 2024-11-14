class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid input. Please try again.")
            self.menu()

    def create_pin(self):
        self.pin = int(input("Enter your pin number: "))
        print(f" PIN created successfully! and Your pin number is {self.pin}")
        self.menu()

    def deposit(self):
        temp = int(input("Enter your pin number: "))
        if temp == self.pin:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"${amount} deposited successfully!")
            self.menu()
        else:
            print("Invalid input. Please try again.")


    # def withdraw(self):
    #     amount = float(input("Enter the amount to withdraw: "))
    #     self.balance -= amount
    #     print(f"${amount} withdrawn successfully!")
    #     self.menu()

