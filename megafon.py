import urllib2
import re
ad = 'https://moscow.shop.megafon.ru/connect/chnumber/fullnumber.html?page=4&search=1&search_area=metall&number_types_filter[7987][0]=7991&'

s = urllib2.urlopen(ad).read()

for i in range (1,3):
 ad1 = 'http://moscow.shop.megafon.ru/connect/chnumber/fullnumber.html?page=%d&search=1&search_area=metall&number_types_filter[7987][0]=7991&' %i
 a = [re.findall('value=("\d{10}")', urllib2.urlopen(ad1).read())]

print a

for i in range (a):
 b[i] = int(a[i])

print b
