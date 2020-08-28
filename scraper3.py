import urllib.request

from bs4 import BeautifulSoup as bs

import threading
import cv2
import sys
import os
import time
import random
import wget
import math
import numpy as np
from math import floor,ceil
#reload(sys)
#sys.setdefaultencoding('utf-8')

class scraper:

	def __init__(self,adress):
		self.xy={}

		self.savePriceFileNameData = {}

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

		results = {}
		p = self.soup.findAll('a',{'title':'View Sales Data'}) 
		prices=([float(x.getText()[1:].replace(',','').replace('$','') )for x in p])
		print('PRICES ',prices)

		if self.siteName == 'ebay':

			a = self.soup.findAll('a',{'class':'b-tile'}) 

			for e in a:

				res = e.findAll('img')

				if res != []:

					results.append(res)

			return results

		else:

			a = self.soup.findAll('h3',{'class':'title'}) 

			for e,i in zip(a,prices):
				#print(e)
				res = e.find('a').getText()

				self.savePriceFileNameData[res]=i

					#print('id ',saveName)
					#results.append(res)


			#return [results,prices]
	def downloadImages(self,results,x,y,j):

		
		j = random.randint(0,100000000000000000000000000000000000)
		i = x
		
		k=list(results.keys())

		for url in k[x:y]:



			path = "image"+str(i)+".jpg"

			#print('url is :',type(url[0]))
			#
			#print(url)
			#attributes = url.attrs

			#tag = attributes['alt']

			#print(tag)

			#self.tags[i]=tag

			


			#print(i)
			#p = urllib.request.urlretrieve(url, 'imgs/image'+str(j)+'.jpg')
			p = wget.download(url)
			#print(p)
			img =np.array(cv2.imread(p,1))

			#print(im.shape)
			#print(type(im))
			z=np.zeros((300,300,3))

			try:
				z[150-floor(img.shape[0]/2):150+ceil(img.shape[0]/2),150-floor(img.shape[1]/2):150+ceil(img.shape[1]/2)] = img/255
			except:
				print('121 error')
			#print(math.floor(300-im.shape[1]),math.ceil(300-im.shape[1]),math.floor(300-im.shape[0]),math.ceil(300-im.shape[0]))
			#z[150-floor(img.shape[0]/2):150+ceil(img.shape[0]/2),150-floor(img.shape[1]/2):150+ceil(img.shape[1]/2)] = img/255
			self.xy[results[url]]=z
			
			#time.sleep(0.3)
			#os.remove(p[0])
			#self.savePriceFileNameData[str(i)]=
			#print('DOWNLOADED')

		

			#print('error with url',url)

			i+=1
	

		

	def threadedDownload(self,NUMBER_OF_DOWNLOADS_PER_THREAD=1):

		x=0

		y=NUMBER_OF_DOWNLOADS_PER_THREAD

		threads = []

		for j in range(len(self.savePriceFileNameData.keys())//NUMBER_OF_DOWNLOADS_PER_THREAD):

			x+=NUMBER_OF_DOWNLOADS_PER_THREAD

			y+=NUMBER_OF_DOWNLOADS_PER_THREAD

			t = threading.Thread(target = self.downloadImages,args =[self.savePriceFileNameData,x,y,j])

			t.start()

			threads.append(t)



		for thread in threads:

			thread.join()

	def scrapeAllImages(self,NUMBER_OF_DOWNLOADS_PER_THREAD=1):

		 self.scrapeImages()
		 self.threadedDownload()
		 return self.xy
