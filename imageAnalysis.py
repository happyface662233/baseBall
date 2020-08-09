import cv2 
ebayImagePath = ''#add your path here
ebay = cv2.imread(ebayImagePath)

picturePath = ''#add your path here 
picture = cv2.imread(picturePath)


res = cv2.matchTemplate(picture,ebay,cv2.TM_CCOEFF_NORMED)
thresh = 0.5 #THIS VALUE NEEDS TWEEKING FOR IT TO WORK WELL

loc = np.where(res>=thresh)
#print(len(res))
for pt in zip(*loc[::-1]):
	print(pt)
	cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
cv2.imshow('detected',img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
