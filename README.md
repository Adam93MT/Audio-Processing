# Audio-Processing

# Assignment 0
The goal of Assignment 0 was to get familiar with working with audio. The task was to write a program to export a Bb note, a B note, and the sum of the two as a wave file.
Since I was more familiar with audio processing in Matlab, so I first wrote it in that. Then to get practice in Python processing, I translated it into Python.

# Assignment 1
## Part 1
This part was to measure the noise floor of a sound card.

## Part 2
The goal of A1.2 was to make a simple, hard knee compressor. 

# Assignment 2
## Part 1
The goal of A2.1 was to recreate the Pasco 9307 Fourier Synthesizer. With a fundamental of 440Hz, we can set the amplitude and phase of the first 9 harmonics.

To run the synth (only tested on MacOS Yosemite), run the command `pythonw synth.py`. Dependencies include: `wave`, `appJar`, `numpy`, `sounddevice`, and `pyplot`

## Part 2
The goal of A2.2 was to add a decay envelope to some of the files generated from the previous section. I wrote this in as the Envelope dropdown box to selevt between a 0.1s, 0.25s decay, or a growth and decay envelope.

![pySynth]('Assignment\ 2/pySynth.png')