from keras import layers
import keras

def makeModel():
	model = keras.Sequential()
	model.add(layers.Conv2D(150,(3,3),activation='relu',input_shape=(300, 300,3)))
	model.add(layers.MaxPooling2D((2,2)))
	model.add(layers.Conv2D(300,(3,3),activation='relu'))
	model.add(layers.MaxPooling2D((2,2)))
	model.add(layers.Conv2D(300,(3,3),activation='relu'))
	model.add(layers.MaxPooling2D((2,2)))
	model.add(layers.Conv2D(600,(3,3),activation='relu'))
	model
	model.add(layers.Dense(300))
	model.add(layers.Dense(200))
	model.add(layers.Flatten())
	model.add(layers.Dense(100,activation = 'relu'))
	
	model.add(layers.Dense(36))#spits out 32 "scores", unique for each pic	model.add(keras.Conv2D(150,activation='relu',input_shape = (300,300,3),))
	model.add(layers.Dense(1))
	model.compile(optimizer='adam',loss = keras.losses.MSE,
		metrics=['accuracy'])
	return model