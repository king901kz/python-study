def bulid_person(first_name,last_name,age=""):
	person = {'first': first_name,'last': last_name}
	
	if age:
		person['age'] = age
	return person

musician = bulid_person('jedl','henderx',19)
print(musician)