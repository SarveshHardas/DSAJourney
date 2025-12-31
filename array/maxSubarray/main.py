import ast

with open("input.txt","r") as f:
    input = ast.literal_eval(f.read())

# solution starts here

current_sum = input[0]
best_sum = input[0]

for num in input[1:]:
    current_sum = max(num,current_sum + num)
    best_sum = max(best_sum,current_sum)


# solution ends here 

with open("output.txt","a") as f:
    f.write(str(best_sum))