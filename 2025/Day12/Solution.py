def parse_input(file_path):
    lines = [line.strip() for line in open(file_path).read().splitlines()]
    boxes = []
    instructions = []

    for line in lines:
        if not line:
            continue
        if line.endswith(':'):
            box = []
            boxes.append(box)
        elif line[0] in '.#':
            box.append(line)
        else:
            assert ': ' in line
            size, counts = line.split(': ')
            size = tuple([int(_) for _ in size.split('x')])
            counts = [int(_) for _ in counts.split()]
            instructions.append((size, counts))

    return (boxes, instructions)
boxes, instructions = parse_input("2025/Day12/input1.txt")
minimum_area=[]
for i in range(0,len(boxes)):
    minimum_area.append(sum(1 for row in boxes[i] for cell in row if cell=='#'))
answer=0
for i in range(0,len(instructions)):
    size, counts = instructions[i]
    area=size[0]*size[1]
    area_needed=0
    for j in range(0,len(boxes)):
        if counts[j]==0:
            continue
        area_needed+=minimum_area[j]*counts[j]
    if area_needed<=area:
        answer+=1
print("First Answer:",answer)