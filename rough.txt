import numpy as np

def frequency_hop(signal, hop_sequence):
    hop_signal = np.zeros_like(signal)
    for i in range(len(signal)):
        hop_signal[i] = signal[i] * hop_sequence[i % len(hop_sequence)]
    return hop_signal

signal = np.array([1, 0, 1, 0, 1, 1, 0, 1])
hop_sequence = np.array([1, 0, 1])
hop_signal = frequency_hop(signal, hop_sequence)

print("Original Signal:", signal)
print("Frequency Hopped Signal:", hop_signal)
