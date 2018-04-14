
import numpy as np
import read_data

def main():
    path = 'data/Sam_full_ROM_set_1_method_1.xlsx'
    data = read_data.main(path)
    new_value = np.zeros([5])
    old_value = np.zeros([5])
    old_diff = np.zeros([5])

    cycle_boo = np.zeros([5])
    cycle_count = np.zeros([5])

    new_high = np.zeros([5])
    old_high = np.zeros([5])
    start_value = np.zeros([5])
    end_value = np.zeros([5])

    mag = np.zeros([5])

    for i_index, value in enumerate(data):
        new_value = value
        new_diff = np.zeros([5])

        for j_index in enumerate(new_value):
            index = j_index[0]
            new_diff[index] = old_value[index] - new_value[index]
            if abs(new_diff[index]) > 2:
                if cycle_boo[index] == 0:
                    start_value[index] = new_value[index]
                    cycle_boo[index] = 1

                if new_diff[index] * old_diff[index] < 0:
                    new_high[index] = new_value[index]
                    mag[index] = new_high[index] - start_value[index]
                    if cycle_boo[index] == 1:
                        cycle_boo[index] = 2
                    elif cycle_boo[index] == 2:
                        cycle_boo[index] = 0
                        cycle_count[index] += 1

        old_value = new_value
        old_diff = new_diff

if __name__ == '__main__':
    main()