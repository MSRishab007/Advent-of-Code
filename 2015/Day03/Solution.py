with open("2015/Day03/input.txt","r") as file:
    directions = file.read().strip()
    visited = set()
    x, y = 0, 0
    m,n=0,0
    visited.add((x, y))
    for index,char in enumerate(directions):
        if index % 2 == 0:
            if char == "^":
                y += 1
            elif char == "v":
                y -= 1
            elif char == "<":
                x -= 1
            elif char == ">":
                x += 1
            visited.add((x, y))
        else:
            if char == "^":
                n += 1
            elif char == "v":
                n -= 1
            elif char == "<":
                m -= 1
            elif char == ">":
                m += 1
            visited.add((m, n))
        visited.add((x, y))
answer=len(visited)
print("First Answer:", answer)