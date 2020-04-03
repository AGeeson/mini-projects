import json

numbers = [2 , 3, 5, 7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


  #saving and and reading user-generated data

  username = input("what is your name?")

  filename = 'username.json'
  with open(filename, 'w') as f_obj:
  	json.dump(username, f_obj) 
  	print("We'll rememvber you when you come back" + username + "!")
  #saves the input to the json file

  import json

  filename = 'username.json'

  with open (filename) as f_obj:
  	username = json.load(f_obj)
  	print("Welcome back," + username + "!")

  	#greet user 

  	import json

  	filename = 'username.json'
  	try: 
  		with open(filename) as f_obj:
  			username = json.load(f_obj)
  		except FileNotFoundError:
  			username = input("what is your name?")
  			json.dump(username, f_obj)
  			print ("We'll remember you when you're back next!" + username)

  		else:
  			print("Welcome back, " + username)


  		"""REFACTORING: process of breaking code up into a series of funcitons that have specific jobs"""
  		#you would refactor the code above by putting it all under one function
  		
