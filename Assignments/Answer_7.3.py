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
