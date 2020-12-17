class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(
            self.customer_id) + "): " + self.first_name + " " + self.last_name + " (" + self.email + ")"


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        # TODO - add validation to prevent misuse
        if amount >= 0:
            self._balance += amount
            print("Deposited: " + str(amount) + ". The new balance is: " + str(self._balance))

    def charge(self, amount):
        #TODO - add validation to prevent misuse
        if amount >= 0:
            if self._balance >= amount:
                self._balance -= amount
                print("Charged: " + str(amount) + ". The new balance is: " + str(self._balance))
            else:
                print("Sorry, you do not have that much money on your account to withdraw: " + amount)


    def calc_interest(self, amount):
        #TODO - add implementation based on self.interest_rate
        self._balance = (self.interest_rate * amount) + amount
        print("the new balance after interest amount is: " + str(self._balance))

    def get_balance(self):
        print("The balance is: " + self._balance)
        return self._balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4} ".format(self.__class__.__name__, self.account_id, self._balance, self.customer.first_name, self.customer.last_name)
        #return self.__class__.__name__ + "(" +  + ")" + " belonging to: " + self.customer.first_name + " " + self.customer.last_name  + " (" + self.customer.email + ")"

    class Bank:
        def __init__(self):
            self.customers = []
            self.accounts = []
            self.transfers = []

            # self.amount = float(input("How much money would you like to put into the account?(USD): "))

        def create_customer(self, first_name, last_name, email):
            c = Customer(first_name, last_name, email)
            self.customers.append(c)
            return c

        def create_account(self, customer):
            a = Account(customer)
            self.accounts.append(a)
            return a

        def create_transfer(self, acc_id_from, acc_id_to, amount):
            # TODO - implement it (input parameters are account ids)
            b = Transfer(acc_id_from, acc_id_to, amount):
            self.transfers.append(b)
            return b

        def transfer(self, acc_from, acc_to, amount):
            # TODO - implement it

            #############################################

            if self.charge(amount) > 0.0:
                acc_to.deposit(amount)
                acc_from.charge(amount)
                return True
            else:
                return False

        def __repr__(self):
            return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)

    bank = Bank()

    c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
    print(c1)
    c2 = bank.create_customer("John", "Kowalski", "j.kowalski@gmail.com")

    a1 = bank.create_account(c1)
    print(a1)
    a2 = bank.create_account(c2)
    print(a1)

    b1 = bank.create_transfer(a1)
    b1 = bank.create_transfer(a2)
    a1.deposit(200)
    a1.charge(100)
    a1.calc_interest(100)
    b1.transfer(100)
    print(bank)
