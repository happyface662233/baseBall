import bs4
import numpy
import cv2
import urllib.request

results = []

pics = []
html = urllib.request.urlopen('https://www.ebay.com/b/Baseball-Trading-Cards/213/bn_2309847?_from=R40&_nkw=&_trksid=m570.l1313%2522')
html = html.read()

soup = bs4.BeautifulSoup(html,'html.parser') #this creates a soup object that gives the html funtionality
a = soup.findAll('a',{'class':'b-guidancecard__link'}) # finds the anchor take with the class 'b-guidancecard__link' and the {} signify a dictionary (aka hash table, linked list. it holds key value pairs

#print(len(a))
#print(type(a))
#print(a[0])
for e in a: #for every anchor tag in the list of anchor tags
	res = e.findAll('img') #in the anchor tag find the img tags
	if res != []: #if it has an image (no img found it will return an empty array
		#print(res)
		results.append(res)#add the image url to the list
		


html = urllib.request.urlopen('https://www.ebay.com/b/Single-Baseball-Trading-Cards/213/bn_17009619?_from=R40&_nkw=') #another page of the ebay page
html = html.read()

soup = bs4.BeautifulSoup(html,'html.parser')
a = soup.findAll('a',{'class':'b-tile'}) 
print(len(a))
print(type(a))
#print(a[0])


#same again
for e in a:
	res = e.findAll('img')
	if res != []:
		results.append(res)
print(len(results))

for i,url in enumerate(results[0:10]): #enumerate is a hard funtion to explain. its a mix of a for each in list loop (for x:xs in js) with the for i in range loops, returning the url and the index
	# url = str.encode(url)
	path = "image"+str(i)+".jpg"#path to save the picture to the disk
	# urllib.request.urlretrieve(url, b''+path)
	#print(url[0])
	attributes = url[0].attrs#gets the html attributes of the html; returns the dictionary

	#urllib.request.urlretrieve(str.encode(str(attributes['src'])), b''+path)
	p = urllib.request.urlretrieve(attributes['src'], path) #in the dictionary of the attributes, find the one that is the image soiurce and save it to the path. save the path where it saved the file as the variable p
	print(p)#print it for troubleshooting
