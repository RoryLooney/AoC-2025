
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

rotations = AoC_file_opener("day1_input.txt")

position = 50
zeros = 0

for rotation in rotations:
    direction = rotation[0]
    rotation = int(rotation.strip(direction))
    
    if direction == "L":
        if (position - rotation) < 0:
            zeros += abs((100 + position - rotation) // 100)
            if position != 0:
                zeros += 1
        position = (position - rotation) % 100
        if position == 0:
            zeros += 1
    elif direction == "R":
        zeros += (position + rotation) // 100
        position = (position + rotation) % 100


print (zeros)

