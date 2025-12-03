import itertools

text=[]
from collections import defaultdict
with open("2025\Day3\input.txt", "r") as file:
    data = file.readline()
    while data:
        text.append(data.strip())
        data = file.readline()
answer=0 
for i in range(0,len(text)):
    current_max=0
    for j in range(0,len(text[i])):
        for k in range(j+1,len(text[i])):
            current_max=max(int(text[i][j]+text[i][k]),current_max)
    answer+=current_max
            
print("First Answer: ",answer)


from functools import lru_cache

def greatest(sequence, allowed=12):

    @lru_cache(None)
    def dfs(index, used):
        if used == allowed:
            return 0
        if len(sequence) - index < allowed - used:
            return -1
        if index == len(sequence):
            return -1
        skip = dfs(index + 1, used)
        take_suffix = dfs(index + 1, used + 1)
        if take_suffix == -1:
            take = -1
        else:
            place = 10 ** (allowed - used - 1)
            take = int(sequence[index]) * place + take_suffix

        return max(skip, take)

    return dfs(0, 0)

answer2 = 0
for s in text:
    x = greatest(s, 12)
    answer2 += x
    

print("Second Answer:", answer2)
