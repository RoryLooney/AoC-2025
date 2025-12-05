
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

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

