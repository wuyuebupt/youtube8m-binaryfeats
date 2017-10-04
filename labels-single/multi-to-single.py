import os,sys
from random import shuffle

if __name__ == '__main__':
	lines = open(sys.argv[1])
	for line in lines:
		# print line.strip()
		arr = line.strip().split(',')
		# print arr[0]
		# print arr[1]
		labels = arr[1].split()
		shuffle(labels)
		shuffle(labels)
		# print labels[0]
		print arr[0], labels[0]
