function [ Aout ] = compressor( A, fs, thresh, Ratio, method )
thresh = - abs(thresh);
dB = 20*log10(abs(A)/1);
T = linspace(0, length(A)/fs, length(A));
sgn = sign(A);
dBout = dB;

for d = [1 : length(dB)]
    if (dB(d) >= thresh)
       dBout(d) = thresh + (dB(d) - thresh)/Ratio; 
    end
end

% figure()
% plot(dB,dB);
figure()
scatter(dB,dBout);

Aout = sgn .* 10.^(dBout./20);

% figure()
% plot(T, dBout)
% title('Compressed dB')
% figure()
% plot(T, Aout)
% title('Compressed File')

end

