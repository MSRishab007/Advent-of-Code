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

answer2=0
for i in range(0,len(text)):
    current_max=0
    for first in range(0,len(text[i])):
        for second in range(first+1,len(text[i])):
            for third in range(second+1,len(text[i])):
                for fourth in range(third+1,len(text[i])):
                    for fifth in range(fourth+1,len(text[i])):
                        for sixth in range(fifth+1,len(text[i])):
                            for seventh in range(sixth+1,len(text[i])):
                                for eighth in range(seventh+1,len(text[i])):
                                    for ninth in range(eighth+1,len(text[i])):
                                        for tenth in range(ninth+1,len(text[i])):
                                            for eleventh in range(tenth+1,len(text[i])):
                                                for twelfth in range(eleventh+1,len(text[i])):
                                                    current_max=max(int(text[i][first]+text[i][second]+text[i][third]+text[i][fourth]+text[i][fifth]+text[i][sixth]+text[i][seventh]+text[i][eighth]+text[i][ninth]+text[i][tenth]+text[i][eleventh]+text[i][twelfth]),current_max)
    print(i, current_max)
    answer2+=current_max        
print("Second Answer: ",answer2)