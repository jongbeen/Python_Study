#숫자의 합. N입력후 N자리 수 모두 10단위로 합

count = input()
count = int(count)

if count >=1 and count<=100:
    cnt=0
    sum=0
    test = input()
    for i in  test:
        sum += int(i)
        cnt +=1

    if cnt == count:
        print(sum)
    
    
