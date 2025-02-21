def merge(numbers, low, mid, high):
    array1 = numbers[low:mid+1]
    array2 = numbers[mid+1:high+1]
    merged_array = []
    i = j = k = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array[low + k] = array1[i]
            i += 1
        else:
            merged_array[low + k] = array2[j]
            j += 1
        k += 1

def mergesort(numbers, low, high):
    if low < high:
        mid = (low + (high-low)//2) 
        mergesort(numbers, low, mid)
        mergesort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)

numbers = [38, 27, 43, 3, 9, 82, 10]
mergesort(numbers, 0, len(numbers)-1)
print(numbers)
