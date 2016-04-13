#Notes 7/4/16

#Using the def assignment to create a neew function, whenever you want a short cut
#Example:

def greeting():
	print 'Hello'

greeting()
greeting()
greeting()
greeting()
greeting()

def addOne(num):
	numPlus = num * 2
	print numPlus

addOne(1)
addOne(3)
addOne(1000)

def home():
	print 'This my house!'

home()

def delt():
	print 'Who smelt it, delt...'

delt()

def pay_calc(h, r):
	pay = h*r
	print pay

hours = float(raw_input('Hours:'))
rate = 13.50

pay_calc(hours,rate)


letter = max('Guessan')
print letter

def name(my, your):
	print "my friend is", my , "your firend is", your

name("bob", "lisa")

#srrr = "lisa"
#name("bob", srrr)
#You can create several place holder within your code, as long as you finalize and declare your variables

#RETURN
def two_plus():
	number = 2 + 325652
	return number 
#not print bc you want to do other stuff with your defined function

eight = two_plus() * 2
print eight
