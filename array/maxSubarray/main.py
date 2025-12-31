import ast

with open("input.txt","r") as f:
    input = ast.literal_eval(f.read())

# solution starts here



# solution ends here 

with open("output.txt","a") as f:
    f.write(str(input))