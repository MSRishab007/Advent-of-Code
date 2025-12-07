with open("2025/Day7/input.txt", "r") as file:
    lines=[line.strip() for line in file.readlines()]
    # print(len(lines),len(lines[0]),len(lines[-1]))
    answer=0
    next_lines=set()
    for i in range(0,len(lines)):
        x=lines[i]
        for j,y in enumerate(x):
            if y=='S':
                next_lines.add(j)
            if y=="^" and j in next_lines:
                next_lines.add(j-1)
                next_lines.add(j+1)
                next_lines.remove(j)
                answer+=1
print("First Answer:",answer)
                
                
            