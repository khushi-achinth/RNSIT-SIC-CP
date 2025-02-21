def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        swapped = False
        for j in range(len(numbers)-i-1):  # Decrease range as the largest elements "bubble" to the end
            if numbers[j] > numbers[j+1]:
                # Swap adjacent elements if they are in the wrong order
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

numbers = [-5,6,3,0,-2,4,7,81,9]
bubble_sort(numbers)
print(numbers)
