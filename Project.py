import math
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# defining the time and frequency axis
multiple = 3
N = multiple * 1024
f = np.linspace(0, 512, int(N / 2))
t = np.linspace(0, 3, 4 * N)


# creating a rectangle function using using step functions
def rect(start, end, domain):
    z = np.reshape([domain >= start], np.shape(domain))
    z1 = np.reshape([domain <= end], np.shape(domain))
    z2 = (z & z1)
    return z2


# defining the right hand and left hand piano notes
notesThird = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3']
notesFourth = ['B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']
# defining the frequency dictionary
frequencies = {'C3': 130.81, 'D3': 146.83, 'E3': 164.81, 'F3': 174.61, 'G3': 196, 'A3': 220, 'B3': 246.93,
               'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392, 'A4': 440, 'B4': 493.88}

# creating a sample song with note duration of 0.1 seconds and gap between notes of 0.2 seconds
# example: looping through Do ri mi fa so la ti do
x = np.zeros_like(t)
i = 0
j = 0
duration = 0.1
gap = 0.2
while i <= 3 - duration:
    x1 = np.sin(2 * np.pi * frequencies[notesThird[j]] * t)
    x2 = np.sin(2 * np.pi * frequencies[notesFourth[j]] * t)
    x = (x1 + x2) * (rect(0 + i, duration + i, t)) + x
    i += gap
    j = (j + 1) % 7

# Scale the signal to avoid clipping
x_max = np.max(np.abs(x))
if x_max > 0:
    x /= x_max


# adding noise by adding random notes to the song
x_f = fft(x)
x_f = 2 / N * np.abs(x_f[0:np.int_(N / 2)])
fn1, fn2 = np.random.randint(0, 512, 2)
n = np.sin(2 * np.pi * fn1 * t) + np.sin(2 * np.pi * fn2 * t)
xNoise = x + n

# removing the noise by removing the noise frequency using the frequency domain
xNoise_f = fft(xNoise)
xNoise_f = 2 / N * np.abs(xNoise_f[0:np.int_(N / 2)])

maxAmp = np.max(x)
peaks = np.where((xNoise_f > maxAmp))[0]
# dividing the indices of largest peaks by the multiple to get the x locations of the required frequencies
fn1hat = int(math.ceil(peaks[0] / multiple))
fn2hat = int(math.ceil(peaks[1] / multiple))
x_filtered = xNoise - (np.sin(2 * np.pi * fn1hat * t) + np.sin(2 * np.pi * fn2hat * t))

x_filtered_f = fft(x_filtered)
x_filtered_f = 2 / N * np.abs(x_filtered_f[0:np.int_(N / 2)])

# Plotting the signals on three different plots
# 1) the song without noise
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("x without noise (time)")
plt.subplot(2, 1, 2)
plt.plot(f, x_f)
plt.title("x without noise (frequency)")
plt.show()

# 2) the song with the noise
plt.subplot(2, 1, 1)

plt.plot(t, xNoise)
plt.title("x with noise (time)")

plt.subplot(2, 1, 2)

plt.plot(f, xNoise_f)
plt.title("x with noise (frequency)")
plt.show()

# 3) the song after filtering the noise
plt.subplot(2, 1, 1)

plt.plot(t, x_filtered)
plt.title("filtered song (time)")

plt.subplot(2, 1, 2)

plt.plot(f, x_filtered_f)
plt.title("filtered song (frequency)")
plt.show()

sd.play(x_filtered, multiple * 1024)
sd.wait()
