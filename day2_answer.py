import re 


def AoC_file_opener(file):
    file = open (file,"r")
    AoC_input = file.read()
    return(AoC_input)
    

AoC_input = AoC_file_opener("day2_input.txt")

ranges = AoC_input.split(",")

all_nums = []

for num_range in ranges:
    num_range = num_range.split("-")

    for i in range(int(num_range[0]),int(num_range[1])+1):
        all_nums.append(i)

total = 0


for i in range(0,len(all_nums)):
    number = str(all_nums[i])
    first_half = number[0:len(str(number))//2]
    last_half = number[len(str(number))//2:len(str(number))]

    if first_half == last_half:
        total += int(number)

print(f"part 1 ans:{total}")



