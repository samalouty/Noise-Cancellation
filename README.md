# Noise Cancelling Project Documentation

This project demonstrates a noise cancelling technique using Python. The code generates a musical signal, adds random noise to it, and then applies a noise removal process to obtain a clean signal. The documentation below explains the signal generation, noise addition, and noise removal steps.

## Signal Generation

The signal generation process involves creating a sample song by combining multiple piano notes. The piano notes used in this project are defined as follows:

- Third Octave Notes: C3, D3, E3, F3, G3, A3, B3
- Fourth Octave Notes: B4, A4, G4, F4, E4, D4, C4

The corresponding frequencies for these notes are defined in a frequency dictionary. The generated song consists of repeated sequences of these notes with a duration of 0.1 seconds each and a gap of 0.2 seconds between each note.

To create the signal, the code loops through the note sequence and generates sinusoidal waves for each note using the defined frequencies. These waves are then added together to form the composite signal.

## Adding Noise

After generating the clean signal, random noise is added to it. The noise is created by generating two random frequencies, `fn1` and `fn2`, and generating sinusoidal waves for these frequencies. These waves are then added to the original signal.

## Noise Removal

The noise removal process is performed in the frequency domain. The code applies the Fast Fourier Transform (FFT) to the noisy signal to obtain its frequency representation. The FFT converts the signal from the time domain to the frequency domain.

The maximum amplitudes of the clean signal are computed, and the frequencies with amplitudes higher than the maximum are identified. The indices of these frequencies are divided by the `multiple` variable to obtain the corresponding frequencies in the original signal.

Using these frequencies, sinusoidal waves are generated, which represent the noise frequencies. The noisy signal is then subtracted by these generated noise waves to obtain a filtered signal.

## Visualization

The resulting signals are visualized in three different plots:

1. **Signal without Noise:** The clean signal is plotted in both the time and frequency domains.
2. **Signal with Noise:** The signal with added noise is plotted in both the time and frequency domains.
3. **Filtered Signal:** The filtered signal, obtained by removing the noise, is plotted in both the time and frequency domains.

Each plot provides a visual representation of the signal at different stages of the noise cancelling process.

## Playback

Lastly, the filtered signal is played back using the `sounddevice` library, allowing you to listen to the noise-cancelled audio.

Please note that this documentation provides a high-level overview of the noise cancelling project. For detailed implementation and understanding, refer to the provided code and relevant comments within the code.

**Note:** Make sure you have the required dependencies installed, such as `numpy`, `sounddevice`, and `matplotlib`, to run the code successfully.

Feel free to modify and experiment with the code to explore different noise cancelling techniques and applications.
