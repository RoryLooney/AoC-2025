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