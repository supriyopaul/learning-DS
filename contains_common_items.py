# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
#For Example:
#const array1 = ['a', 'b', 'c', 'x'];#const array2 = ['z', 'y', 'i'];
#should return false.
#-----------
#const array1 = ['a', 'b', 'c', 'x'];#const array2 = ['z', 'y', 'x'];
#should return true.

# 2 parameters - arrays - no size limit
# return true or false

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'p'];

def contains_common_item(arr1, arr2):
    for element in arr1:
        if element in arr2: return True
    return False

#O(a*b)
#O(1) - Space Complexity

def contains_common_item2(arr1, arr2):
    # loop through first array and create object where properties === items in the array
    # can we assume always 2 params?
    arr1_set = set(arr1)

    # loop through second array and check if item in second array exists on created object.
    for element in arr2:
        if element in arr1_set: return True
    return False

#O(a + b) Time Complexity
#O(a) Space Complexity

# containsCommonItem2(array1, array2)

print(contains_common_item(array1, array2))
print(contains_common_item2(array1, array2))
