def fibbonaci_iterative(num):
    first = 0
    second = 1
    if num == 0: return first
    elif num == 1: return second
    answer = first + second
    for i in range(2, num+1):
        answer = first + second
        first = second
        second = answer
    return answer

def fibbonaci_recursive(num):
    first = 0
    second = 1
    if num == 0: return first
    elif num == 1: return second
    else: return(fibbonaci_recursive(num -1) + fibbonaci_recursive(num -2))


print([fibbonaci_iterative(n) for n in range(0,10)])
print([fibbonaci_recursive(n) for n in range(0,10)])
