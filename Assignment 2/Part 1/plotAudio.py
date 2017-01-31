# import matplotlib.pyplot as plt 
import pylab as p
import numpy as np
import sys 
import csv



with open('audio.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for r, row in enumerate(csvreader):
		if r == 0:
			name = row
		elif r == 1:
			T = row
		elif r == 2:
			D = row

# infile = wave.open('export.wav', 'r')
# spio.wavfile.read('export.wav')

p.figure("Data")
p.plot(T,D)
p.xlim(0,0.01)
plotfile = ''.join(name) + '.png'
print "Saving Plot..." + plotfile
p.savefig(plotfile)