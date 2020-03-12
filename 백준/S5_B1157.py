
sen = input()
sen = list(sen.upper())
alpha = [0]*26

for i in sen:
    alpha[ord(i) - 65] += 1
    
if alpha.count(max(alpha)) >=2:
    print("?")
else:
    # 가장 큰 값의 index + 65는 해당 알파벳이 됨
    print(chr(alpha.index(max(alpha))+65))
