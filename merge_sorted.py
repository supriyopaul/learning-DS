def merge_sorted(arr1, arr2):
    if not arr1: return arr2
    if not arr2: return arr1
    arr1.extend(arr2)
    return sorted(arr1)

def merge_sorted2(arr1, arr2):
    if not arr1: return arr2
    if not arr2: return arr1

    merged_arr = list()
    arr1_element_pos = 0
    arr2_element_pos = 0
    arr1_element = arr1[arr1_element_pos]
    arr2_element = arr2[arr2_element_pos]

    while arr1_element or arr2_element:
        if arr1_element < arr2_element:
            try:
                merged_arr.append(arr1_element)
                arr1_element_pos = arr1_element_pos + 1
                arr1_element = arr1[arr1_element_pos]
            except IndexError:
                arr1_element = None
                break

        else:
            try:
                merged_arr.append(arr2_element)
                arr2_element_pos = arr2_element_pos + 1
                arr2_element = arr1[arr2_element_pos]
            except IndexError:
                arr2_element = None
                break
    import pdb; pdb.set_trace()
    if not arr1_element: merged_arr.extend(arr2[arr2_element_pos:len(arr2)-1])
    if not arr2_element: merged_arr.extend(arr1[arr1_element_pos:len(arr1)-1])

    return merged_arr

print(merge_sorted(['1', '2', '4'], ['3', '5']))
print(merge_sorted(['1', '2', '4'], []))

print(merge_sorted2([1, 2, 4], [3, 5]))
print(merge_sorted2([1, 2, 4], []))
