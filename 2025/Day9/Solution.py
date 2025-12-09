def parse_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    x = [line.strip() for line in lines]
    x=[line.split(",") for line in x]
    x=[[int(i) for i in line] for line in x]
    return x
lines=parse_input("2025/Day9/input.txt")
answer=0
for i in range(0,len(lines)):
    for j in range(i+1,len(lines)):
        x=lines[i]
        y=lines[j]
        area=abs(x[0]-y[0]+1)*abs(x[1]-y[1]+1)
        answer=max(answer,area)
print("First Answer:",answer)
