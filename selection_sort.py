numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
letters = ['z', 'w', 'v', 't', 'k', 'd', 'f', 'a']

def selection_sort(arr):
    end = len(arr)
    for i in range(end):
        smallest_value_index = i
        for j in range(i+1, end):
            if arr[j] < arr[smallest_value_index]:
                smallest_value_index = j
        arr[i], arr[smallest_value_index] = arr[smallest_value_index], arr[i]
        print(arr)
    return arr

print(selection_sort(numbers))
print(selection_sort(letters))
