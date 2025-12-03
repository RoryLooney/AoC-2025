
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

def greedy_search(values,num1,end_num,num2):
    for i in range(values[num1][1]+1,len(bank)-end_num):
        try:
            if values[num2][0] < int(bank[i]):
                values[num2] = (int(bank[i]),i)
        except:
            values.append((int(bank[i]),i))

battery_banks = AoC_file_opener("day3_input.txt")

total_joltage = 0
for bank in battery_banks:
    
    max_value = 0

    for i in range(0,len(bank)):

        for j in range(i+1,len(bank)):

            test_joltage = int(f"{bank[i]}{bank[j]}")
            if test_joltage > max_value:
                max_value = test_joltage

    total_joltage += max_value

print(f"part 1 ans: {total_joltage}")

        
battery_banks = AoC_file_opener("day3_input.txt")

total_joltage = 0

# be greedy! 
# step 1 find biggest digit 12 from last
# step 2 find diggest digit between 11 from last and digit 1
#repeat!

for bank in battery_banks:
    cell_values = []

    for i in range(0,len(bank)-11):
        try:
            if cell_values[0][0] < int(bank[i]):
                cell_values[0] = (int(bank[i]),i)
        except:
            cell_values.append((int(bank[i]),i))

    for i in range(cell_values[0][1]+1,len(bank)-10):
        try:
            if cell_values[1][0] < int(bank[i]):
                cell_values[1] = (int(bank[i]),i)
        except:
            cell_values.append((int(bank[i]),i))

    for i in range(cell_values[1][1]+1,len(bank)-9):
        try:
            if cell_values[2][0] < int(bank[i]):
                cell_values[2] = (int(bank[i]),i)
        except:
            cell_values.append((int(bank[i]),i))

    # i am too lazy to do this properly, but if it works it works!

    greedy_search(cell_values,2,8,3)
    greedy_search(cell_values,3,7,4)
    greedy_search(cell_values,4,6,5)
    greedy_search(cell_values,5,5,6)
    greedy_search(cell_values,6,4,7)
    greedy_search(cell_values,7,3,8)
    greedy_search(cell_values,8,2,9)
    greedy_search(cell_values,9,1,10)
    greedy_search(cell_values,10,0,11)
    
    joltage = ""

    for i in range(0,len(cell_values)):
        joltage =  f"{joltage}{cell_values[i][0]}"

    total_joltage += int(joltage)

print(f"part 2 ans: {total_joltage}")