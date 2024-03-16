#рекурсивная функция для подсчета суммы
def recursionSum(arr):
    if arr == []:
        return 0
    else: 
        return arr[0] + recursionSum(arr[1:])

print(recursionSum([1,3,4])) # 8