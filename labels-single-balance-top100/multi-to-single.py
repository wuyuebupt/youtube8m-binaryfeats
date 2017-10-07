import os,sys
from random import shuffle

if __name__ == '__main__':
	lines = open(sys.argv[1])

	# build sets and back index
	backindex = {}
	for line in lines:
		backindex[line.strip()] = []

	lines = open(sys.argv[2])
	allvideosets = set()
	for line in lines:
		# print line.strip()
		arr = line.strip().split(',')
		allvideosets.add(arr[0])
		# print arr

		# print arr[0]
		labels = arr[1].split()
		for label in labels:
			if label in backindex.keys():
				backindex[label].append(arr[0])
	
	# sample
	keyss = backindex.keys()
	shuffle(keyss)
	for key in keyss:
		# print backindex[key]
		count = 0
		keyvideos = backindex[key]
		shuffle(keyvideos)
		for video in keyvideos:
		# for video in backindex[key]:
			if video in allvideosets:
				print video, key
				allvideosets.remove(video)
				count += 1
			if count == 10000:
				break

			
