f = open('Day3.txt', 'r')
both_wires = (f.read()).splitlines()
f.close()

wire1 = (both_wires[0]).split(',')
wire2 = (both_wires[1]).split(',')

def wire_path(wire, step = False):
    
    x = 0
    y = 0
    steps = 0
    complete_path = []
   
    for i in wire:
        direction = i[0]
        value = int(i[1:])
        
        for j in range(1, value +1):
        
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            
            steps += 1
            
            if step:
                complete_path.append([(x,y), steps])    
            else:
                complete_path.append((x,y)) 
    
    return complete_path



path1 = set(wire_path(wire1))
path2 = set(wire_path(wire2))

intersection = list(path1 & path2)


distance = [sum([abs(point[0]), abs(point[1])]) for point in intersection]
min(distance)

################################
#Part 2

intersection
steps1 = wire_path(wire1, step = True)
steps2 = wire_path(wire2, step = True)

steps_1 = []
for i in steps1:
    if i[0] in intersection:
        steps_1.append(i)

steps_2 = []
for j in steps2:
     if j[0] in intersection:
        steps_2.append(j)


final_steps = []

for n in steps_1:
    
    for m in steps_2:
        if n[0][0] == m[0][0] and n[0][1] == m[0][1]:
            print(n[1] + m[1])
            
        
