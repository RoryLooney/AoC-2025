import re
 
def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input


maths_homework = AoC_file_opener("day6_input.txt")

for i in range(0,len(maths_homework)):
    maths_homework[i] = re.findall("[0-9+*]+",maths_homework[i])

total = 0

for i in range(0,len(maths_homework[0])):

    question_ans = 0

    for j in range(0,len(maths_homework)-1):
        if maths_homework[-1][i] == "+":
            question_ans = question_ans + int(maths_homework[j][i])

        if maths_homework[-1][i] == "*":
            # as 0 * anything is 0 if we are multipling it has to be set to 1
            if question_ans == 0:
                question_ans = 1
            question_ans = question_ans * int(maths_homework[j][i])

    
    total += question_ans

print(f"day 6 part 1 ans: {total}")

#part 2!

maths_homework = AoC_file_opener("day6_input.txt")

adding = False
multing = False
total = 0
running_total = 0

for i in range(0,len(maths_homework[0])):

    if maths_homework[4][i] == maths_homework[3][i] == maths_homework[2][i] == maths_homework[1][i] == maths_homework[0][i]: 
        total += running_total

        running_total = 0

    if maths_homework[4][i] == "+":
        adding = True
        multing = False

    elif maths_homework[4][i] == "*":
        adding = False
        multing = True
    try:
        num = int(f"{maths_homework[0][i]}{maths_homework[1][i]}{maths_homework[2][i]}{maths_homework[3][i]}")
        if adding == True:
            running_total = running_total + num
        if multing == True:
            if running_total == 0:
                running_total = 1
            running_total = running_total * num
    except:
        pass
print(total)
