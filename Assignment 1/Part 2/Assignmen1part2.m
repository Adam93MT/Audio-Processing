close all
oboefile = 'oboe.wav';
trumpetfile = 'trumpet.wav';

[oboe, fs] = audioread(oboefile);
[trumpet, fs] = audioread(trumpetfile);
Toboe = linspace(0, length(oboe)/fs, length(oboe));
Ttrumpet = linspace(0, length(trumpet)/fs, length(trumpet));

%normalize 
oboeNorm = normalize(oboe);
trumpetNorm = normalize(trumpet);

oboeA = normalize(compressor(oboeNorm, fs, 10, 4, 'lin'));
trumpetA = normalize(compressor(trumpetNorm, fs, 10, 4, 'lin'));

oboeB = normalize(compressor(oboeNorm, fs, 20, 20, 'lin'));
trumpetB = normalize(compressor(trumpetNorm, fs, 20, 20, 'lin'));

figure()
plot(Toboe, oboeNorm)
title('Oboe Norm')
figure()
plot(Ttrumpet, trumpetNorm)
title('Trumpet Norm')

figure()
plot(Toboe, oboeA)
title('Oboe CompA')
figure()
plot(Ttrumpet, trumpetA)
title('Trumpet CompA')

figure()
plot(Toboe, oboeB)
title('Oboe CompB')
figure()
plot(Ttrumpet, trumpetB)
title('Trumpet CompB')

audiowrite('results/oboe_norm.wav', oboeNorm, fs);
audiowrite('results/oboe_CompA.wav', oboeA, fs);
audiowrite('results/oboe_CompB.wav', oboeB, fs);
audiowrite('results/trumpet_norm.wav', trumpetNorm, fs);
audiowrite('results/trumpet_CompA.wav', trumpetA, fs);
audiowrite('results/trumpet_CompB.wav', trumpetB, fs);

% trumpQuad = normalize(compressor(trumpetNorm, fs, 10, 4, 'quad'));
% audiowrite('results/trumpet_Quad.wav', trumpQuad, fs);

% trumpLog = normalize(compressor(trumpetNorm, fs, 10, 4, 'log'));
% audiowrite('results/trumpet_Quad.wav', trumpQuad, fs);