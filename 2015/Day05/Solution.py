answer=0
with open("2015/Day05/input.txt") as file:
    words = file.readlines()
    for word in words:
        word=word.strip()
        vowels=0
        double=False
        for i in range(0,len(word)):
            if word[i] in "aeiou":
                vowels+=1
            if i>0 and word[i]==word[i-1]:
                double=True
            if i>0 and (word[i-1:i+1] == "ab" or word[i-1:i+1] == "cd" or word[i-1:i+1] == "pq" or word[i-1:i+1] == "xy"):
                break
        else:
            if vowels>=3 and double:
                answer+=1
    print("First Answer:", answer)
    
answer2=0
with open("2015/Day05/input.txt") as file:
    words = file.readlines()
    for word in words:
        word=word.strip()
        double=False
        pair=False
        for i in range(0,len(word)):
            if i>1 and word[i]==word[i-2]:
                double=True
            if i>0 and word[i-1:i+1] in word[:i-1]:
                pair=True
            if double and pair:
                answer2+=1
                break
    print("Second Answer:", answer2)