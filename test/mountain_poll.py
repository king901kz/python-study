responses = {}


polling_active = True

while polling_active:
	name = input("\nwhat is your name?")
	response = input("\nwhich mountain would you like to climb someday?")
	

	responses[name] = response


	repeat = input("\nwould you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n--- Polling Results ---")
for name,response in responses.items():
	print(name + " would like to clim " + response + ".")
 