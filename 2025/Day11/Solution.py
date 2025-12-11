from collections import defaultdict
def parse_input(filename):
    mapk=defaultdict(list)
    with open(filename,"r") as file:
        for line in file:
            inp=line.split(":")[0]
            outs=line.split(":")[1].strip().split(" ")
            mapk[inp].extend(outs)
    return mapk
mapk=parse_input("2025/Day11/input.txt")
visited=set()
visited.add("you")
def dfs(node,visited):
    if node=="out":
        return 1
    count=0
    for neighbor in mapk[node]:
        if neighbor.islower() and neighbor in visited:
            continue
        visited.add(neighbor)
        count+=dfs(neighbor,visited)
        visited.remove(neighbor)
    return count
answer=dfs("you",visited)
print("First Answer:",answer)
