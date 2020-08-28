
from scraper3 import scraper
import cv2
import numpy as np
from imageAnalysis import feautureMatch
from model import makeModel
import threading
import pickle
import numpy as np
import matplotlib.pyplot as plt 

mx=[]
my=[]
m=makeModel()
ebay = 'https://www.ebay.com/b/Single-Baseball-Trading-Cards/213/bn_17009619?_from=R40&_nkw='
comc = 'https://www.comc.com/Cards/Baseball/'
for i in range(2):
	if i%50 == 0:
		print(i)
		print(len(mx),len(my))
	
	comcScraper = scraper(comc+',p'+str(i))
	xy = comcScraper.scrapeImages()
	xy = comcScraper.savePriceFileNameData
	y= list(xy.keys())
	x = [xy[k] for k in list(xy.keys())]
	print('x,y',len(x),len(y))
	mx+=x
	my+= y
	del comcScraper
	
		#print('faulty url',comc+',p'+str(i))
myx=my
#print('mx: ',mx,'\n\n\n\n\n\n\n\n',my)
print(len(mx),len(my))
'''
with open('mx.p','wb')as c:
	pickle.dump(mx,c)
	c.close()
	
with open('my.p','wb') as f:
	pickle.dump([myx],f)
	'''
print('mx shape ',np.asarray(mx).shape,' my shape ',np.asarray(my).shape)
print(mx[0])
print(mx[-1])
print(my[0])
plt.show()


m.fit(np.asarray(mx),[my],epochs=100,batch_size=16)
