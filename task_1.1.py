arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 1]
def merge(arr1, arr2):
    arr3 = list(set(arr1 + arr2))
    arr3.sort()
    return arr3
merge(arr1, arr2)
