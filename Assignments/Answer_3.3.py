#Assignment: Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:

#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

#Please begin writing the program with the code below:
#score = raw_input("Enter Score: ")

score = raw_input("Enter your score: ")
	#if type(raw_input) == string
	#print "ERROR: Please enter a number score."
	#score = raw_input("Enter your score: ")
elif score <= 0.9:
	print "Your grade is an A"
elif score >= 0.8:
	print "Your grade is a B"
elif score >= 0.7:
	print "Your grade is a C"
elif score >= 0.6:
	print "Your grade is a D"
elif score < 0.6:
	print "Your grade is a F"
if score > 1:
	print "Please enter a score within the range of 0.0 to 1.0"
	raw_input("Enter your score: ")