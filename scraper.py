import urllib.request
from bs4 import BeautifulSoup as bs
import threading
'''
x=0
y=NUMBER_OF_DOWNLOADS_PER_THREAD
threads = []
for _ in range(len(results)//NUMBER_OF_DOWNLOADS_PER_THREAD):
	x+=NUMBER_OF_DOWNLOADS_PER_THREAD
	y+=NUMBER_OF_DOWNLOADS_PER_THREAD
	t = threading.Thread(target = downloadImages,args =[x,y])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

'''
class scraper:
	def __init__(self,adress):
		self.adress = adress 
		self.webPage = urllib.request.urlopen(adress).read()
		self.siteName = self.findName()
		self.soup = bs(self.webPage,'html.parser')
		self.tags = {}
	def findName(self):
		modAdd = self.adress.replace('https://','')
		modAdd = modAdd.replace('www.','')
		return modAdd.split('.')[0]
	def scrapeImages(self):
		results = []
		if self.siteName == 'ebay':
			a = self.soup.findAll('a',{'class':'b-tile'}) 
			for e in a:
				res = e.findAll('img')
				if res != []:
					results.append(res)
			return results
		else:
			a = self.soup.findAll('img',{'class':'cardDetailsImg'}) 
			for e in a:
				res = e.findAll('img')
				if res != []:
					results.append(res)
			return results
	def downloadImages(self,results,x,y):
		reuslts = results[0:5]
		i = x
		for url in results[x:y]:

			path = "image"+str(i)+".jpg"
			#print('url is :',type(url[0]))
			attributes = url[0].attrs
			tag = attributes['alt']
			print(tag)
			self.tags[i]=tag
			try:

				p = urllib.request.urlretrieve(attributes['src'], path)
			except: 
				print('error with url',url)
			i+=1
		
	def threadedDownload(self,results,NUMBER_OF_DOWNLOADS_PER_THREAD=1):
		x=0
		y=NUMBER_OF_DOWNLOADS_PER_THREAD
		threads = []
		for _ in range(len(results)//NUMBER_OF_DOWNLOADS_PER_THREAD):
			x+=NUMBER_OF_DOWNLOADS_PER_THREAD
			y+=NUMBER_OF_DOWNLOADS_PER_THREAD
			t = threading.Thread(target = self.downloadImages,args =[results,x,y])
			t.start()
			threads.append(t)

		for thread in threads:
			thread.join()
	def scrapeAllImages(self,NUMBER_OF_DOWNLOADS_PER_THREAD=1):
		res = self.scrapeImages()
		self.threadedDownload(res)





