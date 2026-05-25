clear;
clc;
close all;

%% Recording settings
Fs = 44100;
nBits = 16;
nChannels = 1;
duration = 15;

%% Record sound
recObj = audiorecorder(Fs, nBits, nChannels);

disp('Start playing the voice conversation on Machine 1...');
disp('Recording started...');
recordblocking(recObj, duration);
disp('Recording finished.');

received_signal = getaudiodata(recObj);

% Save original signal
audiowrite('received_original.wav', received_signal, Fs);

%% Time axis
t = (0:length(received_signal)-1)/Fs;

%% Plot original signal
figure;
plot(t, received_signal);
xlabel('Time [s]');
ylabel('Amplitude');
title('Original Received Voice Signal');
grid on;

%% Band-pass filter for speech
low_cutoff = 300;
high_cutoff = 3400;

[b, a] = butter(6, [low_cutoff high_cutoff]/(Fs/2), 'bandpass');

filtered_signal = filtfilt(b, a, received_signal);

%% Amplification
gain = 4;
processed_signal = gain * filtered_signal;

% Normalize to prevent clipping
processed_signal = processed_signal / max(abs(processed_signal));

% Save processed signal
audiowrite('received_processed.wav', processed_signal, Fs);

%% Plot processed signal
figure;
plot(t, processed_signal);
xlabel('Time [s]');
ylabel('Amplitude');
title('Processed Voice Signal');
grid on;

%% Frequency-domain comparison
N = length(received_signal);
f = (0:N-1)*(Fs/N);

original_fft = abs(fft(received_signal));
processed_fft = abs(fft(processed_signal));

figure;
plot(f(1:floor(N/2)), original_fft(1:floor(N/2)));
xlabel('Frequency [Hz]');
ylabel('Magnitude');
title('Original Signal Spectrum');
grid on;

figure;
plot(f(1:floor(N/2)), processed_fft(1:floor(N/2)));
xlabel('Frequency [Hz]');
ylabel('Magnitude');
title('Processed Signal Spectrum');
grid on;

%% Listen to signals
disp('Playing original received signal...');
sound(received_signal, Fs);
pause(duration + 1);

disp('Playing processed signal...');
sound(processed_signal, Fs);