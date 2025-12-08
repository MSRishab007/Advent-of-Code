from heapq import heapify,heappop, heappush
from collections import defaultdict
def parse_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    x = [line.strip() for line in lines]
    x=[line.split(",") for line in x]
    x=[[int(i) for i in line] for line in x]
    return x
lines=parse_input("2025/Day8/input1.txt")
pairs=[]
for i in range(0,len(lines)):
    for j in range(i+1,len(lines)):
        x=lines[i]
        y=lines[j]
        if i!=j:
            pairs.append(((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2,i,j))
pairs=sorted(pairs,key=lambda x:x[0])
current_new_map_index=0
used=[-1 for i in range(0,1000)]
mapk=defaultdict(int)
for i in range(0,1000):
    distance,point1,point2=pairs[i]
    if used[point1]==-1 and used[point2]==-1:
        used[point1]=current_new_map_index
        used[point2]=current_new_map_index
        mapk[current_new_map_index]+=2
        current_new_map_index+=1
    elif used[point1]!=-1 and used[point2]==-1:
        mapk[used[point1]]+=1
        used[point2]=used[point1]
    elif used[point1]==-1 and used[point2]!=-1:
        mapk[used[point2]]+=1
        used[point1]=used[point2]
    elif used[point1]!=used[point2]:
        mapk[used[point1]]+=mapk[used[point2]]
        mapk[used[point2]]=0
        old_index=used[point2]
        new_index=used[point1]
        for k in range(0,1000):
            if used[k]==old_index:
                used[k]=new_index
answer=0
first_max=1
second_max=1
third_max=1
for i in range(0,current_new_map_index):
    if mapk[i]>first_max:
        third_max=second_max
        second_max=first_max
        first_max=mapk[i]
    elif mapk[i]>second_max:
        third_max=second_max
        second_max=mapk[i]
    elif mapk[i]>third_max:
        third_max=mapk[i]
answer=first_max*second_max*third_max
print("First Answer:",answer)

answer=0
current_new_map_index=0
used=[-1 for i in range(0,1000)]
mapk=defaultdict(int)
for i in range(0,len(pairs)):
    distance,point1,point2=pairs[i]
    if used[point1]==-1 and used[point2]==-1:
        used[point1]=current_new_map_index
        used[point2]=current_new_map_index
        mapk[current_new_map_index]+=2
        current_new_map_index+=1
    elif used[point1]!=-1 and used[point2]==-1:
        mapk[used[point1]]+=1
        used[point2]=used[point1]
    elif used[point1]==-1 and used[point2]!=-1:
        mapk[used[point2]]+=1
        used[point1]=used[point2]
    elif used[point1]!=used[point2]:
        mapk[used[point1]]+=mapk[used[point2]]
        mapk[used[point2]]=0
        old_index=used[point2]
        new_index=used[point1]
        for k in range(0,1000):
            if used[k]==old_index:
                used[k]=new_index
    if mapk[used[point1]]==1000:
        answer=lines[point1][0]*lines[point2][0]
        break
print("Second Answer:",answer)