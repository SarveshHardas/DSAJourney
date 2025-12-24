import ast

with open("input.txt","r") as f:
    input = ast.literal_eval(f.read())
    
# solution starts here

rows = len(input)
cols = len(input[0])

for i in range(1,rows):
    for j in range(1,cols):
        if input[i][j] == 0:
            input[i][0] = 0
            input[0][j] = 0
            
for i in range(1,rows):
    for j in range(1,cols):
        if input[i][0] == 0 or input[0][j] == 0:
            input[i][j] = 0

# solution ends here

with open("output.txt","a") as f:
    f.write(str(input))