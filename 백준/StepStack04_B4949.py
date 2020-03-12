Ans = []
while True:
    Str = input()
    if Str == '.':
        break
    else:
        check = True
        stack = []
        for i in Str:
            if i=='[' or i=='(':
                stack.append(i)
            elif i==']':
                if not stack:
                    Ans.append('no')
                    check = False
                    break
                t = stack.pop()
                if t!='[':
                    check = False
                    Ans.append('no')
                    break
            elif i==')':
                if not stack:
                    Ans.append('no')
                    check=False
                    break
                t = stack.pop()
                if t!='(':
                    check = False
                    Ans.append('no')
                    break
    if check==True:
        Ans.append('yes')

for i in range(len(Ans)):
    print(Ans[i])
