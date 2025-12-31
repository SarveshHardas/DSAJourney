import ast

with open("input.txt","r") as f:
    input = ast.literal_eval(f.read())
    
for i in range(len(input)):
    for j in range(i,len(input)):
        if input[j] < input[i]:
            input[i],input[j] = input[j],input[i]
            
            

with open("output.txt","a") as f:
    f.write(str(input))