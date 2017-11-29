
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist
def balance(accounts):
    for i in range(len(accounts)):
        print(accounts[i]['client_name'], accounts[i]['balance'])

balance(accounts)

print()
def transfer(from_account, to_account, amount):

    if (from_account or to_account) != (11234543 or 43546731 or 23456311):
        print("404 - account not found")

    for i in range(len(accounts)):
        if from_account == accounts[i]['account_number']:
            accounts[i]['balance'] -= amount
            print("Money has been sent from this account:", accounts[i]['client_name'], accounts[i]['balance'])
        if to_account == accounts[i]['account_number']:
            accounts[i]['balance'] += amount
            print("Money has been sent to this account:", accounts[i]['client_name'], accounts[i]['balance'])


transfer(11234543,43546731,100000000)