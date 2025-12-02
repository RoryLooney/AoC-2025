import re 


def AoC_file_opener(file):
    file = open (file,"r")
    AoC_input = file.read()
    return(AoC_input)
    
def remove_odd_lengths(input_list):
    new_list = []
    for i in range(0,len(input_list)):
        if len(str(input_list[i]))%2 ==0:
            new_list.append(input_list[i])
    return(new_list)


AoC_input = AoC_file_opener("day2_input.txt")

ranges = AoC_input.split(",")

all_nums = []

for num_range in ranges:
    num_range = num_range.split("-")

    for i in range(int(num_range[0]),int(num_range[1])+1):
        all_nums.append(i)

# remove all odd lengthed numbers
#all_nums = remove_odd_lengths(all_nums)
total = 0


for i in range(0,len(all_nums)):
    number = str(all_nums[i])
    first_half = number[0:len(str(number))//2]
    last_half = number[len(str(number))//2:len(str(number))]

    if first_half == last_half:
        #print(number)
        total += int(number)

print(f"part 1 ans:{total}")



