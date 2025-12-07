def AoC_file_opener(file):
    file = open (file,"r")
    file.readlines
    AoC_input = []
    for item in file:
        AoC_input.append(item.strip())    
    file.close
    return AoC_input


manifold_diagram = AoC_file_opener("day7_input.txt")
splits = 0
for i in range(0,len(manifold_diagram)):
    
    manifold_diagram[i]= list(manifold_diagram[i])

    for j in range(0,len(manifold_diagram[i])):

        if manifold_diagram[i][j] == "S":
            manifold_diagram[i][j] = "|"

for i in range(0,len(manifold_diagram)-1):
    for j in range(0,len(manifold_diagram[i])):


        if manifold_diagram[i][j] == "|":

            if manifold_diagram[i+1][j] == "^":
                splits += 1
                manifold_diagram[i+1][j-1] = "|" 
                manifold_diagram[i+1][j+1] = "|" 


            elif manifold_diagram[i+1][j] == ".":
                manifold_diagram[i+1][j] = "|"



print(f"day 7 part 1 ans: {splits}")    