# Class Notes for May 7th, 2016
import urllib
from BeautifulSoup import *

url = raw_input ('Enter - ')

openurl = urllib.urlopen(url).read()

soup = BeautifulSoup(openurl)

tags = soup('a')

print tags
