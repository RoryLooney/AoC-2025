
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

def range_checker(big_ranges):
    ranges = list(big_ranges.keys())
    for i in range(0,len(ranges)):
        ranges[i]=ranges[i].split("-")
    big_ranges = {}

    for i in range(0,len(ranges)):
        for j in range(0,len(ranges)):


            #case when the starting range is completly inside another
            if int(ranges[j][0])<int(ranges[i][0])<int(ranges[i][1])<int(ranges[j][1]):
                ranges[i] = [ranges[i][0],ranges[j][1]]
            #case when ends are the same
            elif int(ranges[i][1])==int(ranges[j][1]):
                if int(ranges[i][0]) > int(ranges[j][0]):
                    ranges[i] = [ranges[j][0],ranges[i][1]]
                else:
                    ranges[i] = [ranges[i][0],ranges[i][1]]
            #case when starts are the same
            elif int(ranges[i][0])==int(ranges[j][0]):
                if int(ranges[i][1]) > int(ranges[j][1]):
                    ranges[i] = [ranges[i][0],ranges[i][1]]
                else:
                    ranges[i] = [ranges[j][0],ranges[j][1]]
            #case when first ends inside the second range
            elif int(ranges[i][0])<int(ranges[j][0])<int(ranges[i][1])<int(ranges[j][1]):
                ranges[i] = [ranges[i][0],ranges[j][1]]
            #case when first range starts in the second range
            elif int(ranges[j][0])<int(ranges[i][0])<int(ranges[j][1])<int(ranges[i][1]):
                ranges[i] = [ranges[j][0],ranges[i][1]]



        big_ranges[f"{ranges[i][0]}-{ranges[i][1]}"]="1"

    return big_ranges
    

#too lazy to do the nessacry parsing in code so make sure to seperate ids and ranges before running!
ranges = AoC_file_opener("test.txt")
freshness_ids = AoC_file_opener("tesr2.txt")

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

total_fresh_ids = 0
big_ranges_dict = {}
for line in ranges:
    big_ranges_dict[line]="1"

for i in range(0,1000):
    big_ranges_dict = range_checker(big_ranges_dict)


ranges = list(big_ranges_dict.keys())
for i in range(0,len(ranges)):
    ranges[i]=ranges[i].split("-")
for line in ranges:
    total_fresh_ids += int(line[1])-int(line[0])+1

print(total_fresh_ids)
    


    
