import os
import csv
import wave
import struct
from datetime import datetime as dt
from appJar import gui
import numpy as np
import sounddevice as sd
try:
	del data
except Exception as e:
	pass
try:
	del audio
except Exception as e:
	pass

global bitRate
bitRate = 16
global fs 
fs = 44100
global dur 
dur = 2
global length
length = fs*dur
global harmonics 
harmonics = 9
global T 
T = np.linspace(0, dur, length)
global E
E = np.linspace(1,1,length)

# top slice - CREATE the GUI
app = gui()

app.addLabel("title", "pySYNTH", 0, 4, 3)

app.addLabel("Harm1", "Harmonic 1", 1, 1, 1)
app.setLabelBg("Harm1", "#BADA55")
app.addLabel("Harm2", "Harmonic 2", 1, 2, 1)
app.setLabelBg("Harm2", "#9D8AE6")
app.addLabel("Harm3", "Harmonic 3", 1, 3, 1)
app.setLabelBg("Harm3", "#BADA55")
app.addLabel("Harm4", "Harmonic 4", 1, 4, 1)
app.setLabelBg("Harm4", "#9D8AE6")
app.addLabel("Harm5", "Harmonic 5", 1, 5, 1)
app.setLabelBg("Harm5", "#BADA55")
app.addLabel("Harm6", "Harmonic 6", 1, 6, 1)
app.setLabelBg("Harm6", "#9D8AE6")
app.addLabel("Harm7", "Harmonic 7", 1, 7, 1)
app.setLabelBg("Harm7", "#BADA55")
app.addLabel("Harm8", "Harmonic 8", 1, 8, 1)
app.setLabelBg("Harm8", "#9D8AE6")
app.addLabel("Harm9", "Harmonic 9", 1, 9, 1)
app.setLabelBg("Harm9", "#BADA55")

app.addCheckBox("ON 1", 2, 1)
app.setCheckBox("ON 1", True)
app.addCheckBox("ON 2", 2, 2)
app.addCheckBox("ON 3", 2, 3)
app.addCheckBox("ON 4", 2, 4)
app.addCheckBox("ON 5", 2, 5)
app.addCheckBox("ON 6", 2, 6)
app.addCheckBox("ON 7", 2, 7)
app.addCheckBox("ON 8", 2, 8)
app.addCheckBox("ON 9", 2, 9)

def play(param):
	audio = normalize(compileAudio())
	sd.play(audio, fs)

def export(param):
	# audio = normalize(compileAudio())
	exportAudio()

def setPreset(param):
	preset = app.getOptionBox("Presets")
	if preset == "None":
		pass
	elif preset == "Sine":
		setSine()
	elif preset == "Square":
		setSquare()
	elif preset == "Triangle":
		setTriangle()
	elif preset == "Sawtooth":
		setSawtooth()
	elif preset == "Arbitrary":
		setArb()
	else: return

# def setEnv(param):
# 	env = app.getOptionBox("Envelope")
# 	if env == "None":
# 		pass
# 	else: setEnvelope(env)

app.addLabelNumericEntry("Amp1", 3, 1)
app.setEntry("Amp1", 1)
app.addLabelNumericEntry("Amp2", 3, 2)
app.setEntry("Amp2", 1)
app.addLabelNumericEntry("Amp3", 3, 3)
app.setEntry("Amp3", 1)
app.addLabelNumericEntry("Amp4", 3, 4)
app.setEntry("Amp4", 1)
app.addLabelNumericEntry("Amp5", 3, 5)
app.setEntry("Amp5", 1)
app.addLabelNumericEntry("Amp6", 3, 6)
app.setEntry("Amp6", 1)
app.addLabelNumericEntry("Amp7", 3, 7)
app.setEntry("Amp7", 1)
app.addLabelNumericEntry("Amp8", 3, 8)
app.setEntry("Amp8", 1)
app.addLabelNumericEntry("Amp9", 3, 9)
app.setEntry("Amp9", 1)

app.addLabelNumericEntry("Phase1", 4, 1)
app.setEntry("Phase1", 0)
app.addLabelNumericEntry("Phase2", 4, 2)
app.setEntry("Phase2", 0)
app.addLabelNumericEntry("Phase3", 4, 3)
app.setEntry("Phase3", 0)
app.addLabelNumericEntry("Phase4", 4, 4)
app.setEntry("Phase4", 0)
app.addLabelNumericEntry("Phase5", 4, 5)
app.setEntry("Phase5", 0)
app.addLabelNumericEntry("Phase6", 4, 6)
app.setEntry("Phase6", 0)
app.addLabelNumericEntry("Phase7", 4, 7)
app.setEntry("Phase7", 0)
app.addLabelNumericEntry("Phase8", 4, 8)
app.setEntry("Phase8", 0)
app.addLabelNumericEntry("Phase9", 4, 9)
app.setEntry("Phase9", 0)

app.addRadioButton("waveType1", "Cos", 5, 1)
app.addRadioButton("waveType1", "Sin", 6, 1)
app.addRadioButton("waveType2", "Cos", 5, 2)
app.addRadioButton("waveType2", "Sin", 6, 2)
app.addRadioButton("waveType3", "Cos", 5, 3)
app.addRadioButton("waveType3", "Sin", 6, 3)
app.addRadioButton("waveType4", "Cos", 5, 4)
app.addRadioButton("waveType4", "Sin", 6, 4)
app.addRadioButton("waveType5", "Cos", 5, 5)
app.addRadioButton("waveType5", "Sin", 6, 5)
app.addRadioButton("waveType6", "Cos", 5, 6)
app.addRadioButton("waveType6", "Sin", 6, 6)
app.addRadioButton("waveType7", "Cos", 5, 7)
app.addRadioButton("waveType7", "Sin", 6, 7)
app.addRadioButton("waveType8", "Cos", 5, 8)
app.addRadioButton("waveType8", "Sin", 6, 8)
app.addRadioButton("waveType9", "Cos", 5, 9)
app.addRadioButton("waveType9", "Sin", 6, 9)

app.addNamedButton("Play", "play", play, 7, 4, 1)
app.addNamedButton("Export", "export", export, 7, 5, 1)

app.addLabelOptionBox("Presets", ["None", "Sine", "Square", "Triangle", "Sawtooth", "Arbitrary"], 8, 4, 1)
app.addLabelOptionBox("Envelope", ["None", "0.1s", "0.25s", "Growth-Decay", "0"], 8, 5, 1)
# app.addNamedButton("Set", "setPreset", setPreset, 8, 5, 1)
app.setOptionBoxFunction("Presets", setPreset)
# app.setOptionBoxFunction("Envelope", setEnv)

# ------------ HERE'S THE INTERRESTING STUFF ------------ #
f1 = 440*2*np.pi

def compileAudio():
	print "Compiling..."
	On = [False] * harmonics
	Type = [""] * harmonics
	Amp = [0] * harmonics
	Phase = [0] * harmonics
	for h in xrange(1,harmonics):
		On[h-1] = app.getCheckBox("ON " + str(h))
		if On[h-1]:
			Type[h-1] = app.getRadioButton("waveType" + str(h))
			Amp[h-1] = app.getEntry("Amp" + str(h))
			Phase[h-1] = float(app.getEntry("Phase" + str(h))) * (np.pi/float(180))
			if h == 1:
				data = Amp[h-1] * np.cos(f1*T + Phase[h-1])
			else: 
				data += Amp[h-1] * np.cos(f1*h*T + Phase[h-1])
	return data * getEnvelope()

def exportAudio():
	audio = normalize(compileAudio())
	now = getNowString()
	filename = getFilename() + ".wav"
	outfile = wave.open(filename, 'w')
	outfile.setparams((1, 2, fs, 0, 'NONE', 'not compressed'))
	audio_packed = []
	for s in range(0,length):
		audio_bit = normalizeBit(audio[s])
		audio_packed.append(struct.pack('h',audio_bit))
	# print np.max(abs(audio_bit))
	audio_str = ''.join(audio_packed)

	outfile.writeframes(audio_str)
	print "Exporting: " + filename

	plotAudio(T,audio)

def setSine():
	app.setCheckBox("ON 1", True)
	app.setEntry("Amp1", 1)
	app.setEntry("Phase1", 0)
	app.setRadioButton("waveType1", "Cos")
	for h in xrange(2,10):
		app.setCheckBox("ON " + str(h), False)
		app.setEntry("Amp" + str(h), 0)
		app.setEntry("Phase" + str(h), 0)
		app.setRadioButton("waveType" + str(h), "Cos")

def setSquare():
	for h in xrange(1,harmonics):
		if h%2 == 0:
			app.setCheckBox("ON " + str(h), False)
			app.setEntry("Amp" + str(h), 0)
		else:
			a = 1/float(h)
			wavetype = "Sin"
			app.setCheckBox("ON " + str(h), True)
			app.setEntry("Amp" + str(h), a)
			app.setRadioButton("waveType" + str(h), wavetype)

def setTriangle():
	for h in xrange(1,10):
		if h%2 == 0:
			app.setCheckBox("ON " + str(h), False)
			app.setEntry("Amp" + str(h), 0)
		else:
			a = 1/float(h)**2
			wavetype = "Cos"
			app.setCheckBox("ON " + str(h), True)
			app.setEntry("Amp" + str(h), a)
			app.setRadioButton("waveType" + str(h), wavetype)

def setSawtooth():
	for h in xrange(1,harmonics):
		a = 1/float(h)
		phase = 90
		if h%2 == 0:
			wavetype = "Sin"
		else: wavetype = "Cos"
		app.setCheckBox("ON " + str(h), True)
		app.setEntry("Amp" + str(h), a)
		app.setEntry("Phase" +str(h), phase)
		app.setRadioButton("waveType" + str(h), wavetype)

def setArb():
	a = [.05, .15, .22, .22, .17, .10, .05, .02, .008]
	phase = [0, 180, 0, -180, 0, 180, 0, -180, 0]
	wavetype = "Cos"
	for h in xrange(1,10):
		app.setCheckBox("ON " + str(h), True)
		app.setEntry("Amp" + str(h), a[h-1])
		app.setEntry("Phase" +str(h), phase[h-1])
		app.setRadioButton("waveType" + str(h), wavetype)

def getEnvelope():
	env = app.getOptionBox("Envelope")
	if env == "0.1s":
		E = np.exp(-T/0.1)
	elif env == "0.25s":
		E = np.exp(-T/0.25)
	elif env == "Growth-Decay":
		E = np.linspace(1, 1, length)
		E1 = 1 - np.exp(-T[0 : length/2]/0.1)
		E2 = np.exp(-(T[length/2 : length] - 1)/0.25)
		E = np.append(E1,E2,0)
	elif env == "0":
		E = 0
	else:
		E = 1
	# print "E " + str(E)
	return E

def normalize(data):
	return data/np.max(abs(data))

def normalizeBit(data):
	audio_bit = int(data * (2**(bitRate-1)))
	return audio_bit - np.sign(audio_bit)

def plotAudio(T,audio):
	print "Plotting..."
	with open('results/audio.csv', 'wb') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		now = getNowString()
		csvwriter.writerow(getFilename())
		csvwriter.writerow(T)
		csvwriter.writerow(audio)
	os.system("python plotAudio.py")

def getNowString():
	now = str(dt.now().isoformat())
	now.replace('-', ':')
	return now[0:10] + "-" + now[11:19]

def getFilename():
	preset = app.getOptionBox("Presets")
	env = app.getOptionBox("Envelope")
	if preset != "None":
		filename = preset
	else:
		filename = "Export-" + getNowString()
	if env != "None":
		filename += "-" + env
	filename.replace("/", "-")
	filename.replace(":", "-")
	return "results/" + filename


# bottom slice - START the GUI
app.go()