#9.You are given two sorted arrays that contain only integers. Your task is to find a way to merge them into a single one, sorted in ascending order. Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

arr1 = [1, 4, 3, 4, 5, 11]
arr2 = [6, 6, 8, 9, 10]
arr3 = sorted(arr1 + arr2)
x = list(set(arr3))
print (x)
