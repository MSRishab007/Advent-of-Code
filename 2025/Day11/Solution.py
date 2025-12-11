from collections import defaultdict
from functools import cache
def parse_input(filename):
    mapk=defaultdict(list)
    with open(filename,"r") as file:
        for line in file:
            inp=line.split(":")[0]
            outs=line.split(":")[1].strip().split(" ")
            mapk[inp].extend(outs)
    return mapk
mapk=parse_input("2025/Day11/input.txt")
@cache
def helper(node):
    if node=="out":
        return 1
    count=0
    for neighbor in mapk[node]:
        count+=helper(neighbor)
    return count
answer=helper("you")
print("First Answer:",answer)

@cache
def helper2(node,visited_dac=False,visited_fft=False):
    if node=="out" and visited_dac and visited_fft:
        return 1
    count=0
    if node=="dac":
        visited_dac=True
    elif node=="fft":
        visited_fft=True
    for neighbor in mapk[node]:
        count+=helper2(neighbor,visited_dac,visited_fft)
    return count

answer=helper2("svr",)
print("Second Answer:",answer)
