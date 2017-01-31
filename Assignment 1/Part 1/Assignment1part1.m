clear all
filename = 'Behringer-UMC202_max_noise_floor.wav';
[test, fs] = audioread(filename);
time = length(test)/fs;
mean = mean(test);
meandB = 20*log10(mean);
stdev = std(test);
stdevdB = 20*log10(stdev);
noise_lvl = stdev*2^15;

fileID = fopen('results/noise_floor.txt','w');
% data = [filename, time, mean, meandB, stdev, noise_lvl];
formatSpec = 'File name: %s\nFile length (sec): %2.2f\nMean value: %2.2e\n(Mean value in dB): %4.2fdB\nSTD: %2.2e\nRelative noise level: %2.2f\n';
fprintf(fileID,formatSpec, filename, time, mean, meandB, stdev, noise_lvl);
fclose(fileID);