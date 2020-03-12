
num = input()
table = [0,0,0]

def checkHan(num):
    if num <= 0:
        return False
    elif num<100:
        return True
    elif num>=100 and num <1000:
        index=0
        for i in str(num):
            table[index] = int(i) 
            index+=1
        c1 = table[1] - table[0]
        c2 = table[2] - table[1]
        
        if c2 == c1:
            return True
        else:
            return False
    else:
        return False

test=1
count=0
while test <= int(num):
    if checkHan(test) == True:
        count+=1
        test+=1
    else :
        test+=1
print(count)
 
