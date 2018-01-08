'use strict';

var accounts = [
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
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function balance(bank_accounts) {
	for(var i = 0; i < bank_accounts.length;i++) {
		console.log(bank_accounts[i].client_name + " " + bank_accounts[i].balance);
	}
}

balance(accounts)

function transfer(from_account, to_account, amount, bank_accounts){

	if((from_account || to_account) != (11234543 || 43546731 || 23456311)) {
		console.log("404 - account not found");
	}

	for(var i = 0; i < bank_accounts.length;i++) {
		if(from_account == bank_accounts[i].account_number) {
			bank_accounts[i].balance -= amount;
			console.log("Money has been sent from this account: " + bank_accounts[i].client_name + " " + bank_accounts[i].balance);
		}
		if(to_account == bank_accounts[i].account_number) {
			bank_accounts[i].balance += amount;
			console.log("Money has been sent to this account: " + bank_accounts[i].client_name + " " + bank_accounts[i].balance);
		}
	}
}


transfer(11234543, 43546731, 100000000, accounts);