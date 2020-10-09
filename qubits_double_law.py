import matplotlib.pyplot as plt
import numpy as np
from final_project import dwave_qubits, dwave_year

# Receive lists of data to plot graph
year = dwave_year
num_qubits = dwave_qubits

# Assign first elements as starting point
y0, n0 = year[0], num_qubits[0]

# Create data for the axis
y = np.linspace(y0, year[-1], year[-1] - y0 + 1)

# That parameter shows that values doubles every 2 years
T2 = 2

# Write a formula
double_law = np.log10(n0) + (y - y0) / T2 * np.log10(2)


# Plotting data
plt.plot(year, np.log10(num_qubits), '*', markersize=12, color='r',
         markeredgecolor='r', label='observed')

plt.plot(year, np.poly1d(np.polyfit(year, np.log10(num_qubits), 1))
         (year), label='polyfit')

plt.legend(fontsize=12, loc='upper left')
plt.xlabel('Year', fontsize=12)
plt.ylabel('log(num_qubtis)', fontsize=12)
plt.title('Qubits exponential growth', fontsize=16)

# Save a figure as jpg in static folder

plt.savefig('static/noisy_qubits.jpg', dpi=300)
