current=50
answer=0
with open("2025\Day1\input.txt", "r") as file:
    data = file.readline()
    while data:
        direction, value = data[0], int(data[1:])
        # print(direction, value)
        if direction == "L":
            current -= value    
        else:
            current += value
        current%=100
        if current == 0:
            answer +=1
        data = file.readline()
print("First Answer:",answer)

current=50
answer=0
with open("2025\Day1\input.txt", "r") as file:
    data = file.readline()
    while data:
        direction, value = data[0], int(data[1:])
        # print(direction, value)
        answer+=value//100
        value%=100
        for i in range(0, value):
            if direction == "L":
                current-=1
            else:
                current +=1
            current%=100
            if current==0:
                answer+=1
        current%=100
        data = file.readline()
print("Second Answer:",answer)


current = 50
answer = 0

with open("2025\Day1\input.txt", "r") as file:
    data = file.readline()
    while data:
        direction, value = data[0], int(data[1:])
        answer += value // 100
        value %= 100
        if direction == "L":
            if current !=0 and (current - value) <= 0:
                answer += 1
            current -= value
        else:
            current += value
            if current >= 100:
                answer += 1
        current %= 100
        
        data = file.readline()

print("Second Answer(Updated):",answer)