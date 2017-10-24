

'''

ATM simulation -
Include: check balance, deposit an amount, check a withdrawal amount, withdraw amount, calculate interest
v2 create a user reciept or list of transactions
v3 allow user to enter commands in to a REPL

'''


class Atm:

    def __init__(self, balance=100, interest_rate=.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def check_interest(self):
        return self.interest_rate

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('you deposited: $' + str(amount))
        return self.balance

    def check_withdraw(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append('you withdrew: $' +str(amount))
        return self.balance

    def calc_interest(self):
        earn_interest = self.balance * (1 + self.interest_rate)
        # anticipated amount = balance(1 + (interest_rate*time))
        return earn_interest

    def print_transations(self):
        #for recpt in self.transactions:
        #    print(recpt)
        return '\n'.join(self.transactions)

    def __str__(self):
        return



atm = Atm()

# print('This is the balance of your account: $' + str(atm.balance))
# print('Your current interest rate is: %' + str(atm.interest_rate))
#
# atm.deposit(40)
# print('This is the balance of your account: $' + str(atm.balance))
#
# atm.withdraw(50)
# print('This is the balance of your account: $' + str(atm.balance))
#
# can_i_withdraw = atm.check_withdraw(130)
# print('Checking the ability to withdraw that ammount: ', can_i_withdraw)
#
# # print(cash.calc_interest)






def main():
    print('Welcome to the Bank ATM')
    while True:
        command = input('Check Balance | Check Interest Rate | Deposit | Withdraw | Session Transactions | Exit\nType Command: ').lower()
        if command in ('done', 'quit', 'exit'):
            break
        elif command in('balance', 'check balance'):
            print('\tAccount Balance: $', atm.check_balance())
        elif command in('interest', 'check interest', 'interest rate'):
            print('\tCurrent account Interest Rate: ',atm.check_interest(), '%')
        elif command == 'deposit':
            cash_in = int(input('How much would you like to deposit: '))
            atm.deposit(cash_in)
            print('\tUpdated Account Balance: $', atm.check_balance())
        elif command == 'withdraw':
            cash_out = int(input('How much would you like to withdraw: '))
            atm.withdraw(cash_out)
            print('\tUpdated Account Balance: $', atm.check_balance())
        elif command in('transaction', 'transactions', 'session transactions', 'session'):
            print(atm.print_transations())
        else:
            print('***  command not recognized  ***')

main()