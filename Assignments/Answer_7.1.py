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