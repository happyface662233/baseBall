import bs4
import numpy
import cv2
import urllib.request

results = []

pics = []
html = urllib.request.urlopen('https://www.ebay.com/b/Baseball-Trading-Cards/213/bn_2309847?_from=R40&_nkw=&_trksid=m570.l1313%2522')
html = html.read()

soup = bs4.BeautifulSoup(html,'html.parser')
a = soup.findAll('a',{'class':'b-guidancecard__link'}) 
#print(len(a))
#print(type(a))
#print(a[0])
for e in a:
	res = e.findAll('img')
	if res != []:
		#print(res)
		results.append(res)
		pass


html = urllib.request.urlopen('https://www.ebay.com/b/Single-Baseball-Trading-Cards/213/bn_17009619?_from=R40&_nkw=')
html = html.read()

soup = bs4.BeautifulSoup(html,'html.parser')
a = soup.findAll('a',{'class':'b-tile'}) 
print(len(a))
print(type(a))
#print(a[0])
for e in a:
	res = e.findAll('img')
	if res != []:
		results.append(res)
print(len(results))

for i,url in enumerate(results[0:10]):
	# url = str.encode(url)
	path = "image"+str(i)+".jpg"
	# urllib.request.urlretrieve(url, b''+path)
	#print(url[0])
	attributes = url[0].attrs

	#urllib.request.urlretrieve(str.encode(str(attributes['src'])), b''+path)
	p = urllib.request.urlretrieve(attributes['src'], path)
	print(p)