
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

def neighbour_checker(x_cord,y_cord,x_offest,y_offest,y_max,x_max):

    if y_cord+y_offest < 0 or x_cord+x_offest < 0:
        return(0)
    if y_cord + y_offest > y_max or x_cord + x_offest > x_max:
        return(0)

    if paper_roll_map[y_cord+y_offest][x_cord+x_offest] == "@":
        return(1)
    else:
        return(0)


paper_roll_map = AoC_file_opener("day4_input.txt")
avialable_rolls = 0

for y in range(0,len(paper_roll_map)):

    x_max = len(paper_roll_map[y])-1
    y_max = len(paper_roll_map)-1

    for x in range(0,len(paper_roll_map[y])):
        at_count = 0

        if paper_roll_map[y][x] == "@":

            at_count += neighbour_checker(x,y,1,1,y_max,x_max)
            at_count += neighbour_checker(x,y,1,0,y_max,x_max)
            at_count += neighbour_checker(x,y,1,-1,y_max,x_max)
            at_count += neighbour_checker(x,y,0,1,y_max,x_max)
            at_count += neighbour_checker(x,y,0,-1,y_max,x_max)
            at_count += neighbour_checker(x,y,-1,1,y_max,x_max)
            at_count += neighbour_checker(x,y,-1,0,y_max,x_max)
            at_count += neighbour_checker(x,y,-1,-1,y_max,x_max)

            if at_count < 4:
                avialable_rolls += 1


print(f"part 1 ans: {avialable_rolls}")



