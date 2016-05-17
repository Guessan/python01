#4.6
#raw_input hours and rate per hours to compute gross pay. Change to float
#Award time-and-a-half for the hourly rate for all hrs worked above 40h
#Put the logic to compute time 1/2 pay as function computepay() and use 
#float() to convert the #string to a number. 
#Do not use sum()

hours = raw_input("Enter worked hours: ")
hours = float(hours)
rate = raw_input("Enter hourly rate: ")
rate = float(rate)
def computepay():
	return (40 * rate) + ((rate*1.5) * (hours-40))
if hours > 40.0:
	computepay()
	print "Your Gross Pay is: ", computepay()
elif hours <= 40.0:
	total = hours * rate
	print "Your Gross Pay is: ", total



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


#6.5
#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

#Please use the line below:
text = "X-DSPAM-Confidence:    0.8475";
text_num = text.find('0')
new_num = [text_num:]
continue
print new_num
	#how can I assign this to the variable new_num?
	#new_num = float(new_num)
	#print new_num



#7.1
#Write a program that prompts for a file name, then opens #that file and reads through the file, 
#and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.

#You can download the sample data at http://www.pythonlearn.com/code/words.txt

#Begin to write the program with the following code below:
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fhand = open(fname)
print fhand.upper()



#7.3
#Write a program that prompts for a file name, then opens #that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute 
#the average of those values and produce an output as shown #below. 
#Do not use the sum() function or a variable named sum in #your solution.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
#when you are testing below enter mbox-short.txt as the #file name.

fname = raw_input("Enter file name: ")
fh = open(fname)
file = fh.read()
count = 0
for line in file :
	if line.startswith ('X-DSPAM-Confidence:    0.8475'):
		line = line.rstrip()
		print line
		#How do I assign the new lines as a new file
		newfile = line
		count = count + 1
		print 'Count: ', count
	#How do I extract the int
	for newline in newfile :
		print newfile.find('0')
		#How do I grab those strings, then change them into floats, then sum them up
		#k = list ()
		#newfile.append(k)
		#print len(k)
		#k[0:to the end] and then add them?



#8.4
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt


#Begin to write the program with the following code below:
fname = raw_input("Enter file name: ")
fh = open(fname)
fh = fh.split()
lst = list()
fh.append(lst)
for wrd in lst :
	print wrd.rstrip()



#8.5
#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person 
#who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt


#Begin to write the program with the following code below:
#fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

#fh = open(fname)
#count = 0

