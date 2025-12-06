data=[]
with open("2025\Day6\input.txt", "r") as file:
    for i in range (0,4):
        x = file.readline().strip().split(" ")
        x=[int(i) for i in x if i!=""]
        data.append(x)
    x = file.readline().strip().split(" ")
    x=[i for i in x if i!=""]
    data.append(x)
answer=0

for i in zip(data[0],data[1],data[2],data[3],data[4]):
    a,b,c,d,e=i
    if e=="+":
        answer+=a+b+c+d
    elif e=="*":
        answer+=a*b*c*d
print("First Answer:",answer)
