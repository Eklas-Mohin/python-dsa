def main():
    given_array = [-1, 2, 4, -3, 5, 7, -5, 6]
    array_length = len(given_array)
    number_of_subarrays = 0
    maximum_subarray_sum = float('-inf')

    for i in range(array_length):
        cnt = 0
        for j in range(i, array_length):
            cnt += given_array[j]
            maximum_subarray_sum = max(maximum_subarray_sum, cnt)
            number_of_subarrays += 1

    print("Total number of subarrays:", number_of_subarrays)
    print("Maximum subarray sum:", maximum_subarray_sum)

if __name__ == '__main__':
    main()
