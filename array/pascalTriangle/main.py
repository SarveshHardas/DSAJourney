with open("input.txt","r") as f:
    input = f.readline()
    
# solution starts here

numRows = int(input)
ans = [[0] * numRows for _ in range(numRows)]

for i in range(numRows):
    ans[i][0] = 1
    ans[i][i] = 1
    for j in range(1,i):
        ans[i][j] = ans[i-1][j-1] + ans[i-1][j]


# solution ends here
with open("output.txt","a") as f:
    for i in range(len(ans)):
        while ans[i] and ans[i][-1] == 0:
            ans[i].pop()

    f.writelines(str(ans))