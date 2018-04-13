import xlrd
import numpy as np
from matplotlib import pyplot as plt

# Handle the incoming data
book = xlrd.open_workbook('angle_data_full_ROM.xlsx')
col_elements = len(book._sharedstrings[2].split(","))
row_elements = len(book._sharedstrings)
data_array = np.zeros([row_elements, col_elements])
diff_array = np.zeros([row_elements - 1, col_elements])
for index_i, value in enumerate(book._sharedstrings):
    data_temp = value.split(",")
    for index_j, data in enumerate(data_temp):
        try:
            data_array[index_i, index_j] = float(data)
        except ValueError:
            pass

# Calculate the derivative of the data
for index in range(col_elements):
    diff_array[:, index] = np.diff(data_array[:, index])

# Add time values to the data table
value = 0
for index in range(row_elements):
    data_array[index, col_elements-1] = value
    value += 20

# Plot data
fig, axs = plt.subplots(nrows=4, ncols=1, sharex=True, figsize = [11,11])
x = data_array[:, 4]
for index in range(0,4):
    ax = axs[index]
    y = data_array[:, index]
    ax.plot(x, y)
    major_ticks = np.arange(0, 360, 20)
    ax.set_ylim([0, 360])
    ax.set_yticks(major_ticks)
    ax.grid(which='both')

plt.tight_layout()
plt.show()