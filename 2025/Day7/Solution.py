from functools import cache
def parse_input(filename):
    with open(filename, "r") as file:
        lines=[list(line.strip() )for line in file.readlines()]
    return lines
lines = parse_input("2025/Day7/input.txt")
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

@cache
def helper(current_line,current_position):
    if current_line>=len(lines):
        return 1
    if lines[current_line][current_position]==".":
        return helper(current_line+2,current_position)
    elif lines[current_line][current_position]=="^":
        return helper(current_line+2,current_position-1)+helper(current_line+2,current_position+1)

s_postition=0
for i in lines[0]:
    if i=="S":
        break
    s_postition+=1
answer=helper(2,s_postition)
print("Second Answer:",answer)