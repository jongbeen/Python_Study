
num = input().split()

ascending = True
descending = True

for i in range(1,len(num)):
    if num[i-1] > num[i]:
        ascending = False
    else:
        descending = False

if ascending == True:
    print('ascending')
elif descending == True:
    print('descending')
else:
    print("?")

    
