
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input

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

        

        