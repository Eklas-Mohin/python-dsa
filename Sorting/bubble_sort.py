def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    print('Before Sorting', *arr,)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    print('After Sorting ', *arr)

if __name__ == '__main__':
    main()