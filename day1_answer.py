
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

rotations = AoC_file_opener("day1_input.txt")
start = 50
zeros = 0

for rotation in rotations:
    if rotation[0] == "L":
        start = start - int(rotation.strip("L"))

    else:
        start = start + int(rotation.strip("R"))

    divisor = start // 100
    start = start%100

    if start == 0:
        zeros += 1 +abs(divisor)

print (zeros)
print(abs(-102))
