""" This program finds the number of inversions of a given array in a file"""
import sys
from profilehooks import profile


@profile
def mergeinvfind(array, first, last):
    """ This function merges two given subarrays and counts
        the no of inversoions"""
    if (first == last):
        return [array[first]], 0
    mid = int((last + first)/2)
    result_left, inversions_left = mergeinvfind(array, first, mid)
    result_right, inversions_right = mergeinvfind(array, mid + 1, last)

    arr_1_ind = 0
    arr_2_ind = 0
    left_len = len(result_left)
    right_len = len(result_right)
    result = []
    inversions = inversions_left + inversions_right
    while (arr_1_ind < left_len and arr_2_ind < right_len):
        if (result_left[arr_1_ind] > result_right[arr_2_ind]):
            inversions += (left_len - arr_1_ind)
            result.append(result_right[arr_2_ind])
            arr_2_ind += 1
        else:
            result.append(result_left[arr_1_ind])
            arr_1_ind += 1
    result.extend(result_left[arr_1_ind:])
    result.extend(result_right[arr_2_ind:])
    return result, inversions


@profile
def main():
    """main proc of the program"""
    if (len(sys.argv) < 1):
        sys.stderr.write('Please enter a valid file name to read array from\n')
        return
    array = []
    with open(sys.argv[1], 'r') as inp_file:
        for line in inp_file.readlines():
            array.append(int(line))
    print("Found %d Inversions" % (mergeinvfind(array, 0, len(array)-1)[1]))

if __name__ == "__main__":
    main()
