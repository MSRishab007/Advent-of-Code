answer=0
grid=[[0 for i in range(0,1000)] for j in range(0,1000)]
with open("2015/Day06/input.txt") as file:
    lines=file.readlines()
    for line in lines:
        line=line.strip()
        if line.startswith("turn on"):
            line=line[8:]
            command=1
        elif line.startswith("turn off"):
            line=line[9:]
            command=0
        else:
            line=line[7:]
            command=2
        start,end=line.split(" through ")
        x1,y1=[int(i) for i in start.split(",")]
        x2,y2=[int(i) for i in end.split(",")]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if command==0:
                    grid[i][j]=0
                elif command==1:
                    grid[i][j]=1
                else:
                    grid[i][j]+=1
                    grid[i][j]=grid[i][j]%2
for i in range(0,1000):
    for j in range(0,1000):
        if grid[i][j]==1:
            answer+=1
print("First answer:",answer)


answer2=0
grid=[[0 for i in range(0,1000)] for j in range(0,1000)]
with open("2015/Day06/input.txt") as file:
    lines=file.readlines()
    for line in lines:
        line=line.strip()
        if line.startswith("turn on"):
            line=line[8:]
            command=1
        elif line.startswith("turn off"):
            line=line[9:]
            command=0
        else:
            line=line[7:]
            command=2
        start,end=line.split(" through ")
        x1,y1=[int(i) for i in start.split(",")]
        x2,y2=[int(i) for i in end.split(",")]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if command==0:
                    grid[i][j]=max(0,grid[i][j]-1)
                elif command==1:
                    grid[i][j]+=1
                else:
                    grid[i][j]+=2
for i in range(0,1000):
    for j in range(0,1000):
        answer2+=grid[i][j]
print("Second answer:",answer2)