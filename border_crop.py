import cv2, time, glob
import numpy as np
from PIL import Image

THRESHOLD = 5

def border_check(src, mode=0):
	# mode=0:horizontal scan
	# mode>0:vertical scan
	
	if mode:
		src = np.transpose(src)

	positive_area = []
	_, thresh = cv2.threshold(src, THRESHOLD, 255, cv2.THRESH_TOZERO)
	
	for i in range(len(thresh)):
		pixels = thresh[i]
		filterd_pixel = list(filter(lambda x: True if x else False, pixels))

		if len(filterd_pixel):
			positive_area.append(i)
	
	if len(positive_area):
		# return the border of the positive signal(one dimension)
		return min(positive_area), max(positive_area) + 1

	else:
		# if the whole black image detected, then return original resolution
		return 0, src.shape[0]



def crop_process(src, dir_):
	ext = src.split('.')[-1]
	assert ext in ['jpg', 'gif', 'png'], '格式不符'

	# read & convert
	img = Image.open(src).convert(mode = 'RGB')
	img = np.asarray(img)

	# find contours
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	x1, x2 = border_check(gray, 1)
	y1, y2 = border_check(gray, 0)
	# print(src)
	# print(x1, x2, y1, y2)
	print(x2-x1, y2-y1)

	crop = img[y1:y2, x1:x2]
	img = Image.fromarray(crop)

	if ext == 'gif':
		img = img.convert(mode = 'P', colors = 256, palette = Image.ADAPTIVE)
											 
	img.save('{}/{}_crop.{}'.format(dir_, src.split('.')[-2].split('/')[-1], ext))

print(THRESHOLD)

if __name__ == '__main__':
	t1 = time.time()

	crop_process('./')

	t2 = time.time()
	print('done, 耗時{:5.4f}秒'.format(t2-t1))