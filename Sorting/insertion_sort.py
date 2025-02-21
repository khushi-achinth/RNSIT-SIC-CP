import sys
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

arr = ['F','f','b','B','g','A']
print("Sorted array is:", insertion_sort(arr))
