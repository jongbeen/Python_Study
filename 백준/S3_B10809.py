
test = input()
table = list()
alpha  = range(97,123)
             
for i in alpha:
    if test.find(chr(i))!=-1:
        table.append(test.find(chr(i)))
    else:
        table.append(-1)

for i in range(0,26):
    print(table[i], end=' ' )
    
