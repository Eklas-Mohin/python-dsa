def main():
    given_array = [-1, 2, 4, -3, 5, 7, -5, 6]
    n = len(given_array)
    maximum_subarray_sum = float('-inf')
    cnt = 0

    for i in range(n):
        cnt += given_array[i]
        cnt = max(cnt, given_array[i])
        maximum_subarray_sum = max(cnt, maximum_subarray_sum)

    print("Total number of subarrays:", (n * (n + 1)) // 2)
    print("Maximum subarray sum:", maximum_subarray_sum)

if __name__ == '__main__':
    main()

