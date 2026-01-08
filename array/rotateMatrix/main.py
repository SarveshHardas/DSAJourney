with open("input.txt","r") as f:
    matrix = eval(f.read())
    
n = len(matrix)
# solution starts here
for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue
        if i < j:
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        if j < i:
            continue

for row in matrix:
    row.reverse()     

# solution ends here

with open("output.txt","a") as f:
    f.writelines(str(matrix))