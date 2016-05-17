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