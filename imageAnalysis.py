import cv2 
import numpy as np
def feautureMatch(userInput, webImage, tag):
	ebay = cv2.imread(webImage)

	#picturePath = 'image1.jpg'
	picture = cv2.imread(userInput)


	res = cv2.matchTemplate(picture,ebay,cv2.TM_CCOEFF_NORMED)
	thresh = 0.5
	loc = np.where(res>=thresh)
	#print(len(res))
	if len(loc)>0:
		return tag
	else:
		return None
#def featureMatchList(userInput)