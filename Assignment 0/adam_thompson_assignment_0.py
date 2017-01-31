
# -*- coding: utf-8 -*-
import wave
import math
import struct

pi = math.pi
fs = 44100
bitRate = 16
length = 5 # seconds
samples = list(xrange(0,length*fs))
freq_Bb = 233.082
freq_B = 246.942
A = math.pow(10,-10.0/20.0) # normalized
A = math.pow(2,bitRate-1) * A
# print A

# # (nchannels, sampwidth, framerate, nframes, comptype, compname),
outfile_Bb = wave.open('part1.wav', 'w')
outfile_Bb.setparams((1, bitRate/8, fs, 0, 'NONE', 'not compressed'))

outfile_Bb_inv = wave.open('part1_inv.wav', 'w')
outfile_Bb_inv.setparams((1, bitRate/8, fs, 0, 'NONE', 'not compressed'))

outfile_B = wave.open('part2.wav', 'w')
outfile_B.setparams((1, bitRate/8, fs, 0, 'NONE', 'not compressed'))

outfile_sum = wave.open('part3.wav', 'w')
outfile_sum.setparams((1, bitRate/8, fs, 0, 'NONE', 'not compressed'))

Bb = []
Bb_inv = []
B = []
Sum = []
for s in samples:
	t = s/float(fs)
	val_Bb = A*math.cos(freq_Bb*2*pi * t)
	print val_Bb
	val_Bb_packed = struct.pack('h',val_Bb)
	Bb.append(val_Bb_packed)
	
	Bb_inv.append(struct.pack('h',-val_Bb))

	val_B = A*math.cos(freq_B*2*pi * t)
	val_B_packed = struct.pack('h',val_B)
	B.append(val_B_packed)

	val_sum = val_Bb + val_B
	val_sum_packed = struct.pack('h',val_sum)
	Sum.append(val_sum_packed)	

Bb_str = ''.join(Bb)
outfile_Bb.writeframes(Bb_str)

Bb_inv_str = ''.join(Bb_inv)
outfile_Bb_inv.writeframes(Bb_inv_str)

B_str = ''.join(B)
outfile_B.writeframes(B_str)
	
Sum_str = ''.join(Sum)
outfile_sum.writeframes(Sum_str)

# calculate wavelengths 
c = 343
len_Bb = c/freq_Bb
len_B = c/freq_B

print len_Bb
print len_B

# with open('wavelengths.txt','wb') as outfile:
# 	ostring = 'λ1 = ' + str(len_Bb) + ', λ2 = ' + str(len_B)
# 	outfile.write(ostring.encode('utf-8'))





