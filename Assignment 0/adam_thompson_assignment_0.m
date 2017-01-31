fs = 44100;
l = 2; %seconds
time = 0:l*fs;
freq_Bb3 = 233.082;
freq_B3 = 246.942;
A = 10^(-10/20); % -10dBFS

signal = zeros(1,l*fs+1);

for s = 1:l*fs+1
    t = s/fs;
   signal(s) = A * cos(t * freq_Bb3*2*pi); 
end

plot(time, signal)

audiowrite('Bb.wav',signal,fs)