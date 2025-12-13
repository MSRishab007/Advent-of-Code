answer=0
answer2=1000000
with open("2015/Day01/input.txt") as file:
    for i,char in enumerate(file.read()):
        if char == "(":
            answer += 1
        elif char == ")":
            answer -= 1
        if answer==-1:
            answer2=min(answer2,i)
print("First Answer:", answer)
print("Second Answer:", answer2+1)