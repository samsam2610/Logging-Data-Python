
import numpy as np
import read_data
from matplotlib import pyplot as plt

def main():
    path = 'data/Sam_full_ROM_set_1_method_3.xlsx'
    data = read_data.main(path)

    ax = read_data.group_plot(data)

    current_value = np.zeros([4])
    pre_1st_value = np.zeros([4])
    pre_2nd_value = np.zeros([4])
    pre_3rd_value = np.zeros([4])

    current_diff = np.zeros([4])
    pre_1st_diff = np.zeros([4])
    pre_2nd_diff = np.zeros([4])
    pre_3rd_diff = np.zeros([4])

    cycle_boo = 0
    cycle_count = 0

    new_peak = np.zeros([4])
    new_high = np.zeros([4])
    current_peak = np.zeros([4])

    old_peak = np.zeros([4])
    current_start_value = np.zeros([4])
    prev_start_value = np.zeros([4])
    end_value = np.zeros([4])
    sign = np.zeros([4])
    end_sign = np.zeros([4])
    start_direction = np.zeros([4])

    current_sign = np.zeros([4])
    prev_sign = np.zeros([4])

    start_sign = np.zeros([4])

    mag = np.zeros([4])
    peak_peak = np.zeros([4])
    peak_boo = np.zeros([4])

    current_loc = np.zeros([4])
    high_loc = np.zeros([4])
    loc = np.zeros([4])

    current_marked_peak = np.zeros([4])

    current_max_start_diff = 0
    current_max_start_index = 0

    end_time = 0

    interval = 20
    for i_index, value in enumerate(data):
        current_value = value[0:4]
        current_loc = np.repeat(value[4], 4)
        current_time = value[4]

        current_diff = current_value - pre_1st_value
        current_sign = current_diff / abs(current_diff)

        peak_boo = np.zeros([4])

        sum_diff = 0
        for sum in enumerate(current_diff):
            sum_diff += abs(sum[1])

        check_count = 0

        if min(abs(prev_start_value)) != 0 and min(abs(end_sign)) != 0:
            for k_index in enumerate(current_value):
                temp_index = k_index[0]
                if current_sign[temp_index] == end_sign[temp_index] * (-1):
                    check_count += 1
        else:
            check_count = 4


        if cycle_boo == 0 and current_time - end_time > 500:
            if check_count >= 3:
                for j_index in enumerate(current_diff):
                    index = j_index[0]
                    if abs(current_max_start_diff) < abs(current_diff[index]) \
                            and abs(current_diff[index]) > 1 \
                            and pre_1st_diff[index] != 0:
                        current_max_start_diff = abs(current_diff[index])
                        current_max_start_index = index


        for j_index in enumerate(current_value):
            index = j_index[0]

            # Peak finding

            if current_sign[index] == prev_sign[index]:
                new_high[index] = current_value[index]
                high_loc[index] = current_loc[index]

            elif current_sign[index] != prev_sign[index] and cycle_boo > 0:
                if current_sign[index] == -1:
                    sign[index] = 1
                else:
                    sign[index] = -1

                if sign[index] * (current_value[index] - new_high[index]) > 0:
                    new_peak[index] = current_value[index]
                    loc[index] = current_loc[index]
                    peak_boo[index] = 1
                else:
                    new_peak[index] = new_high[index]
                    loc[index] = high_loc[index]
                    peak_boo[index] = 1

                if new_peak[index] > current_peak[index]:
                    current_peak[index] = new_peak[index]

                mag[index] = current_peak[index] - current_start_value[index]
                if abs(mag[index]) > 30 \
                        and abs(current_peak[index] - current_marked_peak[index]) > 30 \
                        and current_sign[index] != prev_sign[index]:
                    peak_boo[index] = 1
                    current_marked_peak[index] = current_peak[index]
                    if cycle_boo == 1:
                        cycle_boo = 2
                    ax[index].axvline(x=loc[index], color='#45F112')

            end_value[index] = current_peak[index] - current_value[index]
            if index == current_max_start_index:

                if current_max_start_diff > 2 \
                        and  cycle_boo == 0 \
                        and 0 < abs(pre_1st_diff[index]) < abs(current_diff[index]):

                    check_count = 0
                    if prev_start_value[index] != 0 and end_sign[index] != 0:
                        for k_index in enumerate(current_value):
                            temp_index = k_index[0]
                            if current_sign[temp_index] == end_sign[temp_index] * (-1):
                                check_count += 1
                    else:
                        check_count = 4

                    if check_count >= 3:
                        if prev_start_value[index] != 0 and end_sign[index] != 0:
                            cycle_boo = 1
                            for k_index in enumerate(current_value):
                                temp_index = k_index[0]
                                start_sign[temp_index] = current_sign[temp_index]
                                current_start_value[temp_index] = current_value[temp_index]
                                ax[temp_index].axvline(x=current_loc[temp_index], color='#d62728')  # Red
                                prev_start_value[temp_index] = current_start_value[temp_index]
                        else:
                            cycle_boo = 1
                            for k_index in enumerate(current_value):
                                temp_index = k_index[0]
                                start_sign[temp_index] = current_sign[temp_index]
                                current_start_value[temp_index] = current_value[temp_index]
                                prev_start_value[temp_index] = current_start_value[temp_index]
                                ax[temp_index].axvline(x=current_loc[index], color='#d62728')  # Red

                if cycle_boo == 2:
                    check_count = 0
                    for k_index in enumerate(end_value):
                        temp_index = k_index[0]
                        if abs(end_value[temp_index]) >= 0.85 * abs(mag[temp_index]) \
                                and 0 < abs(pre_1st_diff[temp_index]) < 15 \
                                and 0 < abs(current_diff[temp_index]) < abs(pre_1st_diff[temp_index]) \
                                and current_sign[temp_index] == start_sign[temp_index] * (-1):
                            check_count +=1

                    if check_count >= 3:
                        cycle_boo = 0
                        cycle_count += 1
                        current_peak = np.zeros([4])
                        current_marked_peak = np.zeros([4])
                        current_max_start_diff = 0
                        for k_index in enumerate(current_value):
                            temp_index = k_index[0]
                            end_sign[temp_index] = current_sign[temp_index]
                            ax[temp_index].axvline(x=current_loc[temp_index], color='#d67e27')
                        end_time = value[4]


        prev_sign = current_sign
        pre_3rd_value = pre_2nd_value
        pre_2nd_value = pre_1st_value
        pre_1st_value = current_value

        pre_3rd_diff = pre_2nd_diff
        pre_2nd_diff = pre_1st_diff
        pre_1st_diff = current_diff


    plt.tight_layout()
    plt.show()
    print(cycle_count)
    pass
if __name__ == '__main__':
    main()