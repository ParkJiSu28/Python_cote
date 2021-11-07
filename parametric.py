n, m = map(int, input().split())

arr = list(map(int, input().split()))


def binary_search(array, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in array:
            if x > mid:  # 중간 값이 배열의 원소보다 크면 배열의 원소 - 중간값 합을 더해준다
                total += x - mid

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


print(binary_search(arr, 0, max(arr)))
