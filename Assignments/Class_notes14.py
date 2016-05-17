a = 'hello'
b = 'there'
print a +' '+ b

num = int(float(1.348572))
print num

fruit = "banana"
for letter in fruit:
	print letter

fruit = "banana"
count = 0 
for letter in fruit:
	print count, letter
	count = count + 1

for letter in fruit:
	print letter

s = 'Monty Python'
print s[0:4]
#This prints from the first position called to
	#whatever is right before the last position called
print s[6:7]
print s[0:6]
print s[4:10]

fruit = 'banana'
word = raw_input('Write a word: ')
if word < fruit:
	#the </> signs sort the words alphabetically 
		#but with the < meaning "comes before"
	print 'Word comes after fruit'
elif word > fruit:
	print 'Word comes before fruit'
else:
	print word

type(a)
dir(a)
#Allows you to see the string directory that can be applied
	# to this string 
