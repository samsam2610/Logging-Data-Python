
import numpy as np
import read_data
from matplotlib import pyplot as plt

def main():
    path = 'data/Sam_full_ROM_set_2_method_1.xlsx'
    data = read_data.main(path)

    ax = read_data.group_plot(data)

    current_value = np.zeros([4])
    pre_1st_value = np.zeros([4])
    pre_2nd_value = np.zeros([4])
    pre_3rd_value = np.zeros([4])

    old_diff = np.zeros([4])

    cycle_boo = np.zeros([4])
    cycle_count = np.zeros([4])

    new_peak = np.zeros([4])
    old_peak = np.zeros([4])
    current_start_value = np.zeros([4])
    prev_start_value = np.zeros([4])
    end_value = np.zeros([4])

    mag = np.zeros([4])
    peak_peak = np.zeros([4])

    for i_index, value in enumerate(data):
        current_value = value[0:4]
        loc = value[4]

        new_diff = current_value - pre_1st_value
        sign = new_diff / abs(new_diff)

        sum_diff = 0
        for sum in enumerate(new_diff):
            sum_diff += abs(sum[1])

        for j_index in enumerate(current_value):
            index = j_index[0]
            end_value[index] = new_peak[index] - current_value[index]
            if sum_diff > 5:
                if cycle_boo[index] == 0 \
                        and 0 < abs(old_diff[index]) < abs(new_diff[index]):
                    if prev_start_value[index] != 0:
                        if abs(prev_start_value[index] - current_value[index]) < 10:
                            current_start_value[index] = current_value[index]
                            cycle_boo[index] = 1
                            ax[index].axvline(x=loc, color='#d62728') #Red
                            prev_start_value[index] = current_start_value[index]
                    else:
                        current_start_value[index] = current_value[index]
                        cycle_boo[index] = 1
                        ax[index].axvline(x=loc, color='#d62728')  # Red
                        prev_start_value[index] = current_start_value[index]

                elif cycle_boo[index] == 2 \
                        and 0 < abs(old_diff[index]) < 4 \
                        and abs(end_value[index]) >= 0.95 * abs(mag[index]):
                    cycle_boo[index] = 0
                    cycle_count[index] += 1
                    ax[index].axvline(x=loc, color='#d67e27')
                    print('Info', index)
                    print(i_index, data[i_index, 4])
                    print(' ')


            if new_diff[index] * old_diff[index] < 0 and cycle_boo[index] > 0:
                new_peak[index] = current_value[index]
                mag[index] = new_peak[index] - current_start_value[index]
                if abs(mag[index]) > 20:
                    peak_peak[index] = abs(old_peak[index] - new_peak[index])
                    if cycle_boo[index] == 1:
                        cycle_boo[index] = 2
                    old_peak[index] = new_peak[index]
                    ax[index].axvline(x=loc, color='#45F112')

        pre_1st_value = current_value
        pre_2nd_value = pre_1st_value
        pre_3rd_value = pre_2nd_value
        old_diff = new_diff

    plt.tight_layout()
    plt.show()
    print(cycle_count)
    pass
if __name__ == '__main__':
    main()