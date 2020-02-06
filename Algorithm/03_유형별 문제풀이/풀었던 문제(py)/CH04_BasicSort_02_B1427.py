def quicksort(data):
    if len(data) <=1:
        return data
    
    pivot = data[0]
    
    left = [item for item in data[1:] if pivot <= item]
    right = [item for item in data[1:] if pivot > item]
    
    return quicksort(left)+[pivot]+quicksort(right)

Num = list(input())
Num = quicksort(Num)
print(''.join(Num))
