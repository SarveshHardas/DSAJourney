import ast

with open("input.txt","r") as f:
    nums = ast.literal_eval(f.read())
    
# solution start here
i = len(nums) - 2
while i>=0 and nums[i]>=nums[i+1]:
    i-=1

if i>=0:
    j = len(nums)-1
    while nums[j] <= nums[i]:
        j-=1
    nums[i],nums[j] = nums[j],nums[i]

nums[i+1:] = reversed(nums[i+1:])    

# solution ends here

with open("output.txt","a") as f:
    f.write(str(nums))