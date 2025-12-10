import re

def parse_input(filename):
    required_switch_state=[]
    allowed_combinations=[]
    joltage_requirements=[]
    pattern = re.compile(
        r"^\[([^\]]+)\]\s*((?:\((?:\d+(?:,\d+)*)\)\s*)+)\{([^}]+)\}\s*$"
    )

    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            m = pattern.match(line)
            if m:
                required_switch_state.append([1 if x=="#" else 0 for x in m.group(1)])
                x = m.group(2)
                groups = re.findall(r"\(([^)]*)\)", x)
                group_lists = [list(map(int, g.split(","))) for g in groups]
                allowed_combinations.append(group_lists)
                x = m.group(3)
                joltage_requirements.append(list(map(int, x.split(","))))
                
            else:
                print("No match for line:", line)
    return required_switch_state, allowed_combinations, joltage_requirements
required_switch_state, allowed_combinations, joltage_requirements = parse_input("2025/Day10/input.txt")
answer=0
for i in range(0,len(required_switch_state)):
    req_state = required_switch_state[i]
    allowed_combos = allowed_combinations[i]
    start_state=[0 for j in range(len(req_state))]
    minimum_steps=float('inf')
    queue=[(start_state,0)]
    visited=set()
    while queue:
        a= queue.pop(0)
        state, steps = a
        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if state == req_state:
            minimum_steps = min(minimum_steps, steps)
            continue
        for c in allowed_combos:
            new_state = state[:]
            for index in c:
                new_state[index] = 1 - new_state[index]
            queue.append((new_state, steps + 1))
    answer += minimum_steps
print("First answer:", answer)
