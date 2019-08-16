import zipfile
import numpy as np
import pickle
import os
import logging
validation_counter = 0 
for file_num in range(20425):
	print(file_num)
	with zipfile.ZipFile("./numpys/{}.pickle.zip".format(file_num), 'r') as file:
		file.extractall("./numpys")
	with (open("./numpys/{}.pickle".format(file_num), 'rb')) as file:
		array = np.array(pickle.load(file, encoding = 'latin1'))
	os.remove("./numpys/{}.pickle".format(file_num))
	validation = True
	zero_point = 0
	zero_point = int(zero_point)
	for x in range(19200):
		for y in range(128):
			if array[y,x] == 1 and (y < 21 or y > 107):
				validation	= False
		if type(zero_point) is int:
			if np.sum(array[:,x]) != 0:
				zero_point = False
		if zero_point == False:
			if np.sum(array[:,x]) == 0:
				zero_point = int(x)
	if validation:
		array = array[20:108,:zero_point+768]
		if array.shape[1] > 3072:
			print(array.shape)
			with open("./clean_data/{}.pickle".format(validation_counter), "wb+") as file:
				pickle.dump(array,file)
			validation_counter += 1

