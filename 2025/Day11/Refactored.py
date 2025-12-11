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
@cache
def helper(start_node, end_node):
    if start_node == end_node:
        return 1
    count = 0
    for neighbor in mapk[start_node]:
        count += helper(neighbor, end_node)
    return count
mapk=parse_input("2025/Day11/input.txt")
answer=helper("you", "out")
print("First Answer:",answer)
answer=helper("svr", "dac") * helper("dac", "fft") * helper("fft", "out")+ helper("svr", "fft") * helper("fft", "dac") * helper("dac", "out")
print("Second Answer:",answer)