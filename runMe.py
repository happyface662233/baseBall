from scraper import scraper
import cv2
import numpy as np
from imageAnalysis import feautureMatch
ebay = 'https://www.ebay.com/b/Single-Baseball-Trading-Cards/213/bn_17009619?_from=R40&_nkw='
comc = 'https://www.comc.com/Cards/Baseball/'


ebayScraper = scraper(ebay)
comcScraper = scraper(comc)
while True:
	ebayScraper.scrapeAllImages()
	comcScraper.scrapeAllImages()
	print('scraped all')
	inputPath = input('Enter the path of the picture')
	print(inputPath)
	#inputImage = cv2.imread(inputPath,-1)
	print('img read')
	error = False
	i=0
	while error==False:
		print('in loop')
		'''
		try:
			out = feautureMatch(inputImage,cv2.imread('image'+str(i)+'.jpg'),'tag')
		except:
			error = True
			'''
		out = feautureMatch(inputPath,'image'+str(i)+'.jpg','tag')
		print(out)
	print('done loop')
print('done')

