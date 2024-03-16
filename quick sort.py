#быстрая сортировка
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greatest = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greatest)

print(quickSort([3,6,1])) # 1 3 6
