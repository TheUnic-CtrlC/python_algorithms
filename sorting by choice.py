#нахождения индекса минимального элемента массива
def findSmaller(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i
    return smaller_index

#добавление минимального элемента массива в новый массив с последующим возвратом
def selectionSort(arr):
    newArr = []
    for i in range (len(arr)):
        smaller = findSmaller(arr)
        newArr.append(arr.pop(smaller)) # pop удаляет элемент массива с последующим возвратом индекса
    return newArr

print(selectionSort([3,4,5,7,1,-6,9])) # [-6, 1, 3, 4, 5, 7, 9]

