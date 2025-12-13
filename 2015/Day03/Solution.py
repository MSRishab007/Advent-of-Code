with open("2015/Day03/input.txt","r") as file:
    directions = file.read().strip()
    visited = set()
    x, y = 0, 0
    x1,y1 = 0,0
    x2,y2 = 0,0
    visited.add((x, y))
    visited1 = set()
    visited1.add((x1,y1))
    for index,char in enumerate(directions):
        if index % 2 == 0:
            if char == "^":
                y1 += 1
                y+=1
            elif char == "v":
                y1 -= 1
                y-=1
            elif char == "<":
                x1 -= 1
                x-=1
            elif char == ">":
                x1 += 1
                x+=1
            visited1.add((x1, y1))
        else:
            if char == "^":
                y2 += 1
                y+=1
            elif char == "v":
                y2 -= 1
                y-=1
            elif char == "<":
                x2 -= 1
                x-=1
            elif char == ">":
                x2 += 1
                x+=1
            visited1.add((x2, y2))
        
        visited.add((x, y))
answer=len(visited)
answer2=len(visited1)
print("First Answer:", answer)
print("Second Answer:", answer2)