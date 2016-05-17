#Class Notes 21
#for carryon in ['My, Wayward, Son, Therell, Be, Peace, When, You, Are, Done']
#	print carryon
#for SergioIsA in ['potato, head']:
#	print "Sergio is a ", SergioIsA

#friends = ['Joseph', 'Glenn', 'Sally']
#for friend in friends :
#		print 'Happy New Year!', friend
#for i in range(len(friends)) :
#	friend = friend[i]
#	print friend

#a = range(10)
#b = range(10)
#d = [] #same as d = list()

for i in a:
	c = a[i] + b[i]
	d.append(c)
print d

#slicing and indexes are the same in lists as they are in strings
a = [1, 2, 3]

if 2 in a:
	b = a.index[2]
	a[b] = 'hello'
	print a
else :
	 print 'Not in the list'