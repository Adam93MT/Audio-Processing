close all
Sig1file = 'Sig1.wav';
Sig2file = 'Sig2.wav';
Sig3file = 'Sig3.wav';
Sig4file = 'Sig4.wav';

[Sig, fs] = audioread(Sig1file);
Fourier = (fft(Sig));
T = linspace(0,length(Sig)/fs,length(Sig));
freq = linspace(0,fs,length(Fourier));
f1 = 100;

figure()
plot(T,Sig)
xlim([0 1/f1])

figure()
plot(freq,abs(Fourier))
xlim([0 2500])
figure()
plot(freq,angle(Fourier))
xlim([0 1500])
ylim([-3*pi/2 pi/2])

harmonix = [1:25];
harmonics_f = harmonix*f1;
harm_idx = harmonics_f*2 + 1;

mag_harm = abs(Fourier(harm_idx));
mag_harm = mag_harm/max(mag_harm); %normalize
phase_harm = angle(Fourier(harm_idx));
phase_harm = round(phase_harm*pi/2)/(pi/2); %round to the nearest pi/2

figure()
scatter(harmonix, mag_harm)
figure()
scatter(harmonix, phase_harm)

%recreate
for i = harmonix
   if i == 1
       Outsig = mag_harm(i) * cos(harmonics_f(i)*T);
   else
       Outsig = Outsig + mag_harm(i) * cos(harmonics_f(i)*T);
   end
end

figure()
plot(T,Outsig)
xlim([0 1/f1])
