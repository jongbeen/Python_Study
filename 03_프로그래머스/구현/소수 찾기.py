from itertools import permutations
import math

def find(n,p_set):
    array = [True for i in range(n+1)]
    prime_numbers = []
    for i in range(2,int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1
    for i in range(2,n+1):
        if array[i] and i in p_set:
            prime_numbers.append(i)
    return prime_numbers

def solution(numbers):
    p_set = set()
    for i in range(1,len(numbers)+1):
        per_data = permutations(numbers,i)
        for data in per_data:
            d = ''.join(list(data))
            p_set.add(int(d))
    ans = find(max(p_set),p_set)
    print(ans)

    answer = len(ans)
    return answer
print(solution('011'))