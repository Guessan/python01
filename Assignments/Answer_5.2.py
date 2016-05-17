#5.2
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the #numbers. 
#If the user enters anything other than a valid number catch it with a #try/except and put out an appropriate message and ignore #the number.

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
	    if num == "done" : break
    		print num
    	try:
    		num = float(num)

		except:
			return "Please Enter a Number"
			continue
l = list()    
#l.insert(num)
l.append(num)
    for num in l :
		if num > largest :
			largest = num
			#print "This is the largest number: ", largest
		elif num < smallest :
			smallest = num
			#print "This is the smallest number: ", smallest
print "Max: ", largest
print "Min: ", small

