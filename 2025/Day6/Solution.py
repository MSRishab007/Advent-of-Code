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

answer=0
with open("2025\Day6\input.txt", "r") as file:
    first_line = file.readline().strip("\n")[::-1]
    second_line = file.readline().strip("\n")[::-1]
    third_line = file.readline().strip("\n")[::-1]
    fourth_line = file.readline().strip("\n")[::-1]
    operators = [i for i in file.readline().strip().split(" ") if i!=""][::-1]
    operator_index=0
    nums=[]
    for i in zip(first_line, second_line, third_line, fourth_line):
        a,b,c,d=i
        if a==b==c==d==" ":
            if operators[operator_index]=="+":
                answer+=sum(nums)
            elif operators[operator_index]=="*":
                prod=1
                for j in nums:
                    prod*=j
                answer+=prod
            # print("Nums:",nums)
            nums=[]
            operator_index+=1
        else:
            x=a+b+c+d
            x=x.strip()
            if x.isdigit():
                # print(x)
                nums.append(int(x))
if operators[operator_index]=="+":
    answer+=sum(nums)
elif operators[operator_index]=="*":
    prod=1
    for j in nums:
        prod*=j
    answer+=prod
print("Second Answer:",answer)
