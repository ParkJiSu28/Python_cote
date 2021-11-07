import sys, bisect

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())

arr1 = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for x in arr1:
    result = binary_search(arr, x, 0, n - 1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
