'use strict';

const accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log '404 - account not found' if any of the account numbers don't exist to the console.

function balance(bank_accounts) {
	bank_accounts.map(account => {
    console.log(`${account.client_name}: ${account.account_number}`);
  });
}

balance(accounts);

function transfer(from_account, to_account, amount, bank_accounts){
  let valid = 0;
  bank_accounts.map(account => {
    account.account_number === from_account || account.account_number === to_account ?
    valid += 1 : null;
  })

	if(valid !== 2) {
    console.log('404 - account not found');
    return;
  }
  
  bank_accounts.map(account => {
    if (from_account === account.account_number) {
      account.balance -= amount;
			console.log(`Money has been sent from this account: ${account.client_name} ${account.balance}`);
    }
    if (to_account === account.account_number) {
      account.balance += amount;
			console.log(`Money has been sent to this account: ${account.client_name} ${account.balance}`);
    }
  });
}

transfer(11234543, 43546731, 100000000, accounts);
