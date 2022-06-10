import time
start_time = time.perf_counter()

def binarySearch(arr, target, first, last):
    if first > last:
        return 1
    mid = int((first+last)/2)
    if arr[mid]==target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, first, mid-1)
    else:
        return binarySearch(arr, target, mid+1, last)

n = int(input())
lst = list(map(int, input().split()))
result = sorted(lst)

for i in range(n):
    print(binarySearch(result, lst[i], 0, n-1), end=' ')

end_time = time.perf_counter()
print(f"\ntime elapsed : {int(round((end_time - start_time) * 1000))}ms")