with open("2025\Day2\input.txt", "r") as file:
    data = file.readline()
    data=data.split(",")
    data = [[int(i.split("-")[0]),int(i.split("-")[1])] for i in data]
    data.sort()
sum=0
for i in data:
    for j in range(i[0],i[1]+1):
        x=str(j)
        if len(x)%2==0:
            left=x[:len(x)//2]
            right=x[len(x)//2:] 
            if left==right:
                sum+=j
print("First Answer: ",sum)

sum=0
for i in data:
    for j in range(i[0],i[1]+1):
        x=str(j)
        double=x+x
        double=double[1:-1]
        if x in double:
            sum+=j
print("Second Answer: ",sum)