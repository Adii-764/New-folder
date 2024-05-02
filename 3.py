import numpy as np  # Import NumPy library

# Define the optimize_coverage function
def optimize_coverage(signals):
    return np.mean(signals)

# Sample signals for demonstration
signals = [1, 0.5, 0.3, 0.8]

# Calculate the optimized signal using the optimize_coverage function
optimized_signal = optimize_coverage(signals)

# Print the original signals and the optimized signal
print("Original Signals:", signals)
print("Optimized Signal:", optimized_signal)
