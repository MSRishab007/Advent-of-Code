def parse_input(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
        lines=[[int(i) for i in line.strip().split("x")] for line in lines]
    return lines
dimensions=parse_input("2015/Day02/input.txt")
answer=0
answer2=0
for length,width,height in dimensions:
    sides=[length*width,width*height,height*length]
    perimeter=[2*(length+width),2*(width+height),2*(height+length)]
    smallest_perimeter=min(perimeter)
    volume=length*width*height
    ribbon=smallest_perimeter+volume
    surface_area=2*sum(sides)
    extra=min(sides)
    total_area=surface_area+extra
    answer+=total_area
    answer2+=ribbon
print("First Answer:",answer)
print("Second Answer:",answer2)