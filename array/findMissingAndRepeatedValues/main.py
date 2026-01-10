import ast

with open("input.txt","r") as f:
    grid = ast.literal_eval(f.read())

# solution starts here

n = len(grid)
freq = [0] * (n*n + 1)
for i in range(n):
    for j in range(n):
        freq[grid[i][j]] += 1
    
repeating = -1
missing = -1

for num in range(1, n*n + 1):
    if freq[num] == 2:
        repeating = num
    if freq[num] == 0:
        missing = num
    
ans = [repeating, missing] 
    

# solution ends here 

with open("output.txt","a") as f:
    f.write(str(ans))