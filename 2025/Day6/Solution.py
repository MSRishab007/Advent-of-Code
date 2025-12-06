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

answer = 0
with open("2025\Day6\input.txt", "r") as file:
    lines = [file.readline().strip("\n")[::-1] for _ in range(4)]
    operators = [i for i in file.readline().strip().split(" ") if i != ""][::-1]
    
    nums = []
    operator_index = 0
    
    for chars in zip(*lines):
        if all(c == " " for c in chars):
            if nums:
                result = sum(nums) if operators[operator_index] == "+" else 1
                if operators[operator_index] == "*":
                    for n in nums:
                        result *= n
                answer += result
                nums = []
                operator_index += 1
        else:
            x = "".join(chars).strip()
            if x.isdigit():
                nums.append(int(x))
    
    if nums:
        result = sum(nums) if operators[operator_index] == "+" else 1
        if operators[operator_index] == "*":
            for n in nums:
                result *= n
        answer += result

print("Second Answer:", answer)
