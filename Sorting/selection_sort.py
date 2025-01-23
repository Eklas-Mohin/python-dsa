def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    print('Before Sorting:', *arr)

    for i in range(n - 1):
        idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    print('After Sorting:', *arr)

if __name__ == '__main__':
    main()
