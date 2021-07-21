numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
letters = ['z', 'w', 'v', 't', 'k', 'd', 'f', 'a']

def bubble_sort(arr):
    end = len(arr) - 1
    for i in range(end):
        for j in range(end-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            print(arr)
    return arr

print(bubble_sort(numbers))
print(bubble_sort(letters))
