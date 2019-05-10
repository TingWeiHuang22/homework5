from __future__ import print_function
import cv2
import numpy as np



MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 1.0

image_dir = './picture/'
method = 'ORB'
# method = 'SIFT'
# method = 'SURF'
TF = '/TRUE/'
# TF = '/FALSE/'
result_dir = image_dir + method +'/'
film_dir = result_dir+'film/'


def alignImages(im1, im2 , meth='ORB'):
	input_img1 = im1.copy()
	input_img2 = im2.copy()
	# input_img1 = cv2.cvtColor(input_img1, cv2.COLOR_BGR2GRAY)
	# input_img2 = cv2.cvtColor(input_img2, cv2.COLOR_BGR2GRAY)
	if TF == '/TRUE/':
		cross = True
	else:
		cross = False
	print(meth)
	if meth == 'ORB':
		# Detect ORB features and compute descriptors.
		detector = cv2.ORB_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=cross)
		# Convert images to grayscale

	elif meth == 'SURF':
		detector = cv2.xfeatures2d.SURF_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=cross)
	elif meth == 'SIFT':
		detector = cv2.xfeatures2d.SIFT_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=cross)

	keypoints1, descriptors1 = detector.detectAndCompute(input_img1, None)
	keypoints2, descriptors2 = detector.detectAndCompute(input_img2, None)

	# Match features.
	# create BFMatcher object
	# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	# matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
	matches = matcher.match(descriptors1, descriptors2, None)


	# Sort matches by score
	matches.sort(key=lambda x: x.distance, reverse=False)

	# Remove not so good matches
	numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
	matches = matches[:numGoodMatches]

	# print(type(keypoints1))


	# Extract location of good matches
	points1 = np.zeros((len(matches), 2), dtype=np.float32)
	points2 = np.zeros((len(matches), 2), dtype=np.float32)

	new_matches = []
	for i, match in enumerate(matches):
		if keypoints1[match.queryIdx].pt[0]>360 and keypoints1[match.queryIdx].pt[0]<720 and keypoints1[match.queryIdx].pt[1]>270 and keypoints1[match.queryIdx].pt[1]<810:
			if keypoints2[match.queryIdx].pt[0]>360 and keypoints2[match.queryIdx].pt[0]<720 and keypoints2[match.queryIdx].pt[1]>270 and keypoints2[match.queryIdx].pt[1]<810:
				new_matches.append(match)
				points1[i, :] = keypoints1[match.queryIdx].pt
				points2[i, :] = keypoints2[match.trainIdx].pt


	# Draw top matches
	imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, new_matches, None)
	# cv2.imwrite("matches.jpg", imMatches)

	# Find homography
	h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

	# Use homography
	height, width, channels = im2.shape
	im1Reg = cv2.warpPerspective(im1, h, (width, height))

	return im1Reg, h , imMatches , matches , keypoints1 , keypoints2
def cut_center(img,rate):
	height, width, channels = img.shape
	center_h = int(height/2)
	center_w = int(width/2)
	new_center_h = int(height*rate/2)
	new_center_w = int(width*rate/2)
	result = img.copy()
	result = result[center_h-new_center_h:center_h+new_center_h,center_w-new_center_w:center_w+new_center_w,:]
	return result

def combine_images(imgs):
  height0, width0, channels0 = imgs[0].shape
  height, width, channels = imgs[1].shape
  new_img = imgs[0].copy()
  for i in range(1,len(imgs)):
    print("process image %d ..."%i)
    img = imgs[i]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img[:,:,3])
    for x in range(height):
      for y in range(width):
        if img_gray[x,y]!=0:
          new_img[int((height0-height)/2)+x,int((width0-width)/2)+y,:]=img[x,y,:]
  return new_img

def make_loop(img):
  height, width, channels = img.shape
  rate = 0.5
  img2 = cv2.resize(img.copy(),(int(width*rate),int(height*rate)))

  imReg, h = alignImages(img2, img)
  cv2.imwrite(result_dir+"loop.jpg", imReg)
  img_combine = combine_images([img,img2])
  return img_combine

def make_film(img,rate,times):
	img2 = img.copy()
	for i in range(times):
		img2 = cv2.resize(cut_center(img2,rate),(1080,1080))
		outFilename = film_dir+"film%d.jpg"%i
		print("Saving film image : ", outFilename); 
		cv2.imwrite(outFilename, img2)


if __name__ == '__main__':

	refFilename = image_dir+"a3.jpg"
	print("Reading reference image : ", refFilename)
	imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
	imReference = cv2.resize(imReference,(1080,1080))

	imFilename = image_dir+"a4.jpg"
	print("Reading image to align : ", imFilename);  
	im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
	im = cv2.resize(im,(1080,1080))

	imReg, h ,immatch ,matches ,p1 ,p2 = alignImages(im, imReference, method)
	print(dir(matches[0]))
	print(len(matches))
	for i,match in enumerate(matches):
		print(match.distance)
		print(match.imgIdx)
		print(match.queryIdx)
		print(match.trainIdx)
		print(p1[match.queryIdx].pt)
		print(p2[match.trainIdx].pt)
		print('---')
	cv2.imwrite("matches_%s.jpg"%method, immatch)
	cv2.imwrite("ref_%s.jpg"%method, imReference)
	cv2.imwrite("align_%s.jpg"%method, imReg)
	cv2.imwrite("ref_re%s.jpg"%method, imReference[100:,:900,:])
	cv2.imwrite("align_re%s.jpg"%method, imReg[100:,:900,:])
	