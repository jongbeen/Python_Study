a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1,8):
    if a[i-1] > a[i]:
        ascending = False
    else:
        descending = False

if ascending :
    print('ascending')
elif descending :
    print('descending')
else:
    print("?")
