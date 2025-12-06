from pathlib import Path

def calculate_result(nums, operator):
    """Calculate result based on operator."""
    if operator == "+":
        return sum(nums)
    elif operator == "*":
        result = 1
        for n in nums:
            result *= n
        return result
    return 0

def solve():
    file_path = Path(__file__).parent / "input.txt"
    
    with open(file_path, "r") as file:
        lines = [file.readline().strip() for _ in range(4)]
        operators = [i for i in file.readline().strip().split() if i]
    answer1 = sum(
        calculate_result([int(a), int(b), int(c), int(d)], e)
        for a, b, c, d, e in zip(lines[0].split(), lines[1].split(), 
                                  lines[2].split(), lines[3].split(), operators)
    )
    print("First Answer:", answer1)
    
    # Part 2
    reversed_lines = [line[::-1] for line in lines]
    reversed_operators = operators[::-1]
    answer2 = 0
    nums = []
    op_idx = 0
    
    for chars in zip(*reversed_lines):
        if all(c == " " for c in chars):
            if nums:
                answer2 += calculate_result(nums, reversed_operators[op_idx])
                nums = []
                op_idx += 1
        elif (x := "".join(chars).strip()).isdigit():
            nums.append(int(x))
    
    if nums:
        answer2 += calculate_result(nums, reversed_operators[op_idx])
    
    print("Second Answer:", answer2)

solve()
