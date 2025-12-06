import bisect
ranges=[]
checklist=[]
with open("2025\Day5\input1.txt", "r") as file:
    data= file.readline()
    x=data.strip().split("-")
    ranges.append([int(x[0]), int(x[1])])
    while "-" in data:
        data = file.readline()
        if "-" not in data:
            break
        if data:
            x=data.strip().split("-")
            ranges.append([int(x[0]), int(x[1])])
    while data:
        data = file.readline()
        if data:
            checklist.append(int(data.strip()))

ranges.sort(key=lambda x: x[0])
merged_ranges=[]
current_start, current_end = ranges[0]
for i in range(1, len(ranges)):
    if ranges[i][0] <= current_end:
        current_end = max(current_end, ranges[i][1])
    else:
        merged_ranges.append([current_start, current_end])
        current_start, current_end = ranges[i]
merged_ranges.append([current_start, current_end])
start_points = [r[0] for i,r in enumerate(merged_ranges)]

answer=0

for i in checklist:
    idx = bisect.bisect_right(start_points, i) - 1
    if idx >= 0 and merged_ranges[idx][0] <= i <= merged_ranges[idx][1]:
        answer += 1

print("First Answer:", answer)

answer=0
for i in merged_ranges:
    answer += (i[1] - i[0] + 1)
print("Second Answer:", answer)