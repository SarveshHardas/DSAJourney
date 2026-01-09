with open("input.txt","r") as f:
    intervals = eval(f.read())
    
# solution starts here
n = len(intervals)
intervals.sort()
unoverlapped_intervals = []

for i in range(n-1):
    if intervals[i][1] >= intervals[i+1][0]:
        unoverlapped_intervals.append([intervals[i][0],intervals[i+1][1]])
    else:
        unoverlapped_intervals.append(intervals[i+1])

# solution ends here

with open("output.txt","a") as f:
    f.writelines(str(unoverlapped_intervals))