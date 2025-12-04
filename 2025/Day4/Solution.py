rolls = []
with open("2025\Day4\input.txt", "r") as file:
    data = file.readline()
    while data:
        x=[str(i) for i in data.strip()]
        rolls.append(x)
        data = file.readline()
answer = 0
for i in range(0, len(rolls)):
    for j in range(0, len(rolls[i])):
        if rolls[i][j] == "@":
            count=0
            check=[[i-1, j], [i+1, j], [i, j-1], [i, j+1], [i-1, j-1], [i+1, j+1], [i-1, j+1], [i+1, j-1]]
            for k in check:
                if 0 <= k[0] < len(rolls) and 0 <= k[1] < len(rolls[i]) and rolls[k[0]][k[1]] == "@":
                    count += 1
            if count <4:
                answer += 1
print("First Answer:", answer)

answer = 0
while True:
    prev=answer
    removed = set()
    for i in range(0, len(rolls)):
        for j in range(0, len(rolls[i])):
            if rolls[i][j] == "@":
                count=0
                check=[[i-1, j], [i+1, j], [i, j-1], [i, j+1], [i-1, j-1], [i+1, j+1], [i-1, j+1], [i+1, j-1]]
                for k in check:
                    if 0 <= k[0] < len(rolls) and 0 <= k[1] < len(rolls[i]) and rolls[k[0]][k[1]] == "@":
                        count += 1
                if count <4:
                    answer += 1
                    removed.add((i, j))
    for r in removed:
        rolls[r[0]][r[1]] = "."      
    if prev == answer:
        break
        
print("Second Answer:", answer)