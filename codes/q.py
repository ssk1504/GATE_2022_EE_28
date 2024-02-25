import matplotlib.pyplot as plt
import numpy as np

# Read data from data.txt
frequency_range = []
magnitude_response = []
with open("data.txt", "r") as file:
    for line in file:
        x, y = map(float, line.split())
        frequency_range.append(x)
        magnitude_response.append(y)

# Find the index of the peak
peak_index = np.argmax(magnitude_response)
peak_frequency = frequency_range[peak_index]
peak_magnitude = magnitude_response[peak_index]

# Convert frequency to kHz
frequency_range = np.array(frequency_range) / 1000  # Convert Hz to kHz

# Plot the frequency response
plt.figure(figsize=(8, 6))
plt.plot(frequency_range, magnitude_response, color='blue')
plt.scatter(peak_frequency / 1000, peak_magnitude, color='red', label='Peak at {:.1f} kHz'.format(peak_frequency / 1000))
plt.plot([149.750, 150.250], [0.500, 0.500], color='orange', linestyle='--', label='B=600 Hz', marker='.')
plt.title('Frequency Response')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
plt.show()

