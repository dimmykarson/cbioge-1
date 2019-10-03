from keras.layers import *
from keras.models import *

def conv2conv(in_layer):
	layer = Conv2D(32, 3)(in_layer)
	#layer = Conv2D(32, 3)(layer)
	return layer

def conv2drop(in_layer):
	layer = Conv2D(32, 3)(in_layer)
	layer = Dropout(0.1)(layer)
	return layer

def add(in_layer):
	layer = Conv2D(32, 3, padding='same')(in_layer)
	#layer = BatchNormalization()(layer)
	layer = Add()([layer, in_layer])
	return layer

def is_valid_build(input_shape, build):
	in_layer = Input(input_shape)
	out_layer = build(in_layer)
	try:
		model = Model(input=in_layer, output=out_layer)
		model.compile(optimizer='adam', loss='binary_crossentropy')
	except ValueError:
		#print(e)
		return False
	return model is not None

if __name__ == '__main__':
	
	print(is_valid_build((256, 256, 1), conv2conv))
	print(is_valid_build((4, 4, 1), conv2conv))
	print(is_valid_build((3, 3, 1), conv2conv))
	#print(is_valid_build((2, 2, 1), conv2conv)) #error

	#print(is_valid_build((2, 2, 1), conv2drop))#error

	print(is_valid_build((4, 4, 1), add))