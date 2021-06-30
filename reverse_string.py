def reverse(string):
    length = 0
    character_array = list()
    reverse_string = str()
    for character in string:
        character_array.append(character)
        length = length + 1
    for i in range(length-1,-1,-1):
        reverse_string = reverse_string + character_array[i]
    return reverse_string


print(reverse('qwerty'))
