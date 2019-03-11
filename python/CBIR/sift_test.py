import tkinter as tk
import os, sys
import shutil
import time
import cv2
from matplotlib import pyplot as plt 


DBASE="./dbase"
ALGO="./algo"
TEMP="./temp"
cnt = 0
selfile=''
selparent=''

def show_rgb_img(img):
	"""Convenience function to display a typical color image"""
	return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))

def to_gray(color_img):
	gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
	return gray

def gen_sift_features(gray_img):
	sift = cv2.xfeatures2d.SIFT_create()
    # kp is the keypoints
    #
    # desc is the SIFT descriptors, they're 128-dimensional vectors
    # that we can use for our final features
	kp, desc = sift.detectAndCompute(gray_img, None)
	return kp, desc

def show_sift_features(gray_img, color_img, kp):
	return plt.imshow(cv2.drawKeypoints(gray_img, kp, color_img.copy()))


def sift_compute(file1,file2,result):
	global cnt
	global selfile
	global selcategory

	img1 = cv2.imread(file1)
	img2 = cv2.imread(file2)
	#show_rgb_img(img1);
	#plt.show()

	img1_gray = to_gray(img1)
	img2_gray = to_gray(img2)

	#plt.imshow(img1_gray, cmap='gray'),plt.show();
	# generate SIFT keypoints and descriptors
	img1_kp, img1_desc = gen_sift_features(img1_gray)
	img2_kp, img2_desc = gen_sift_features(img2_gray)

	#print ('Here are what our SIFT features look like for the   image:')
	#show_sift_features(img1_gray, img1_front, img1_kp);
	#plt.show()

	# create a BFMatcher object which will match up the SIFT features
	bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
	matches = bf.match(img1_desc, img2_desc)
	# Sort the matches in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)
	file = os.path.basename(file2)
	parent=os.path.basename(os.path.dirname(file2))
	if(len(matches)>= cnt):
		cnt = len(matches)
		selfile = file
		selcategory = parent

	print("{}<><><>{}<><><>{}".format(file2,len(matches),parent))
    
	# draw the top N matches
	N_MATCHES = 100

	match_img = cv2.drawMatches( img1, img1_kp, img2, img2_kp, matches[:N_MATCHES], img2.copy(), flags=0)

	#plt.figure(figsize=(12,6))
	#plt.imshow(match_img);
	#plt.show()
	cv2.imwrite(result,match_img)


def searchFile(your_file):
	global cnt
	global selfile
	global selcategory
	
	cnt=0
	selfile=''
	selparent=''
	
	shutil.rmtree(TEMP, ignore_errors=True)
	os.makedirs(TEMP);
          
	
	print(your_file)
	timestamp = int(time.time()*1000.0)          
	new_file=str(timestamp)+"_"+os.path.basename(your_file)
	algo='SIFT'
	#print(new_folder)
	new_path=TEMP+"/"+new_file
	print(new_path)
	shutil.copy(your_file,new_path)
	#####################
	folders=os.listdir(DBASE)
	i=0
	for folder in folders:
		files = os.listdir(DBASE+"/"+folder)
		print(files)
		for file in files:
			oldpath = DBASE+"/"+folder+"/"+file
			i = i+1
			## ## ## ##
			filename, file_extension = os.path.splitext(oldpath)
			print(new_path)
			result_path = TEMP+"/"+algo+"_"+folder+"_res"+str(i)+file_extension
			sift_compute(new_path,oldpath,result_path)
            
	########################
	print("Result", "Searching database using {} .Result={}"
                                    .format(algo,selcategory))      

your_file='/home/sarath/coding/py_workspace/ui/001.jpeg'	
searchFile(your_file)