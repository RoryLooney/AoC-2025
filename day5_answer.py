
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

def sort_list(list_to_sort):
    for i in range(0,len(list_to_sort)):
        for j in range(0,len(list_to_sort)-1):
            if int(list_to_sort[i][0]) < int(list_to_sort[j][0]):
                list_to_sort[i],list_to_sort[j] = list_to_sort[j],list_to_sort[i]
    return list_to_sort

def check_if_in_range(range_1,range_2):
    lower_bound_range_1,upper_bound_range_1 = int(range_1[0]),int(range_1[1])
    lower_bound_range_2,upper_bound_range_2 = int(range_2[0]),int(range_2[1])

    if upper_bound_range_1 >= lower_bound_range_2: # when true the second range is in some part of range 1
        if upper_bound_range_2>upper_bound_range_1:
            return True, lower_bound_range_1,upper_bound_range_2
        else:
            return True, lower_bound_range_1,upper_bound_range_1
    else:
        return False, lower_bound_range_1,upper_bound_range_1

#too lazy to do the nessacry parsing in code so make sure to seperate ids and ranges before running!
ranges = AoC_file_opener("day5_input_ranges.txt")
freshness_ids = AoC_file_opener("day5_input_ids.txt")

for i in range(0,len(ranges)):
    ranges[i]=ranges[i].split("-")

fresh_items = 0

for id in freshness_ids:
    for freshness_range in ranges:
        if int(id)>=int(freshness_range[0]) and int(id)<=int(freshness_range[1]):
            fresh_items+=1
            break
            
print(f"part 1 ans: {fresh_items}")

#part 2!

ranges = AoC_file_opener("day5_input_ranges.txt")

for i in range(0,len(ranges)):
    ranges[i]=ranges[i].split("-")

sorted_ranges = sort_list(ranges)
current_lower_bound = 0
current_upper_bound = 0
previous_upper_bound = 0
merged_range = False
big_ranges = []

for i in range(0,len(sorted_ranges)-1):

    merged_range,current_lower_bound,current_upper_bound = check_if_in_range(sorted_ranges[i],sorted_ranges[i+1])

    if merged_range == True:
        if previous_upper_bound > current_upper_bound:
            sorted_ranges[i+1]=current_lower_bound,previous_upper_bound
        else:
            sorted_ranges[i+1]=current_lower_bound,current_upper_bound
            previous_upper_bound = current_upper_bound


    elif merged_range == False:
        big_ranges.append(f"{current_lower_bound}-{current_upper_bound}")
        previous_upper_bound = 0

big_ranges.append(f"{current_lower_bound}-{current_upper_bound}")


for i in range(0,len(big_ranges)):
    big_ranges[i]=big_ranges[i].split("-")

total = 0

for line in big_ranges:
    total += int(line[1]) -int(line[0]) +1

print(f"part 2 ans: {total}")
