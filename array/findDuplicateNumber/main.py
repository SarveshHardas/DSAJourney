import ast

with open("input.txt","r") as f:
    nums = ast.literal_eval(f.read())

# solution starts here

nums.sort()

for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        ans = nums[i]
        break

# solution ends here 

with open("output.txt","a") as f:
    f.write(str(ans))