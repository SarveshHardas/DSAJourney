import ast

with open("input.txt","r") as f:
    lines = [line.strip() for line in f if line.strip()]

nums1 = ast.literal_eval(lines[0])
m = int(lines[1])                 
nums2 = ast.literal_eval(lines[2])
n = int(lines[3])
    
# solution starts here

nums1 = [x for x in nums1 if x != 0]
nums2 = [x for x in nums2 if x != 0]

for j in range(len(nums2)):
    for i in range(len(nums1)):
        if nums1[i] > nums2[j]:
            nums1[i],nums2[j] = nums2[j],nums1[i]


nums1 = nums1+nums2

# solution ends here

with open("output.txt","a") as f:
    f.writelines(str(nums1))