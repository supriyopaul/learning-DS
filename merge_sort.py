numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
letters = ['z', 'w', 'v', 't', 'k', 'd', 'f', 'a']

def merge_sort(arr):
    arrsize = len(arr)
    if arrsize == 1: return arr
    mid = int(arrsize/2)
    left = arr[:mid]
    right = arr[mid:]
    print(left, right)
    return merge(merge_sort(left), merge_sort(right))

def merge(l, r):
    i = j = 0
    merged_arr = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged_arr.append(l[i])
            i = i + 1
        else:
            merged_arr.append(r[j])
            j = j + 1
    merged_arr.extend(l[i:])
    merged_arr.extend(r[j:])
    print(merged_arr)
    return merged_arr

print(merge_sort(numbers))
print(merge_sort(letters))
