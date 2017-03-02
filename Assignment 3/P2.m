close all
[trump1, fs] = audioread('trump1.wav');
[trump2, fs] = audioread('trump2.wav');
[oboe1, fs] = audioread('oboe1.wav');
[oboe2, fs] = audioread('oboe2.wav');

Tt = linspace(0,length(trump1)/fs,length(trump1));
To = linspace(0,length(oboe1)/fs,length(oboe1));

% figure()
% plot(Tt, trump1)
% title('trump1')
% figure()
% plot(Tt, trump2)
% title('trump2')
% figure()
% plot(To, oboe1)
% title('oboe1')
% figure()
% plot(To, oboe2)
% title('oboe2')


TRUMP1 = (fft(trump1));
% TRUMP1 = TRUMP1(1:length(TRUMP1)/2);
TRUMP1(abs(TRUMP1) < 1) = 0;
freq = linspace(0,fs/2, length(TRUMP1));
ix = find(abs(TRUMP1) > 1,1); %find first harmonic

TRUMP1a = TRUMP1;
TRUMP2a = TRUMP1;

TRUMP1a(ix) = 0;
TRUMP2a(ix) = TRUMP1(ix)*10^(1/2); 

% figure()
% plot(freq,abs(TRUMP1));
% figure()
% plot(freq,abs(TRUMP1a));
% figure()
% plot(freq,abs(TRUMP2a));

trump1a = ifft(TRUMP1a);
trump2a = ifft(TRUMP2a);

figure()
hold on
plot(Tt, trump1,'b')
plot(Tt,trump1a, 'r')
plot(Tt, trump2a, 'g')

audiowrite('trump1a.wav', trump1a, fs);
audiowrite('trump2a.wav', trump2a, fs);
















