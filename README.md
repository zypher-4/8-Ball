# 8-Ball
## A simple 8 Ball program in Python

### Variables:
	- pred - List, empty on initialization.
	- user_dir - Boolean, False on initialization.

### Functions:
	- import_default()
		imports the default list of predictions.
	- import_user()
		imports the users list of preditions.
	- create_user()
		creates Predictions-User.txt
		executed by default on import.
	- check_user()
		checks if the Predictions-User.txt exists.
	- add_pred(user_pred)
		let's you add into Predictions-User.txt
	- make_pred(temp_pred=pred)
		randomly returns a prediction from Predictions-User.txt or Predictions-Default.txt
	- print_pred
		prints all the possible prediction in Predictions-User.txt and Predictions-Default.txt
