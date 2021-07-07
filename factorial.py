def factorial_iterative(num):
    answer = 1
    while num > 1:
        answer = answer * num
        num = num - 1
    return answer

def factorial_recursive(num):
    answer = 1
    if num == 2:
        return num
    else:
        return (num * factorial_recursive(num - 1))

print(factorial_iterative(5))
print(factorial_recursive(5))
