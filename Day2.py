import copy

#op = [1,9,10,3,2,3,11,0,99,30,40,50]

f = open('Day2.txt', 'r')
content = (f.read()).split(',')
f.close()
content = [int(i) for i in content]

content[1] = 12
content[2] = 2
op = copy.deepcopy(content)

i = 0
while True:
    
    if op[i] == 99:
        break

    instructions = op[i:i+4]
    
    x = op[instructions[1]]
    y = op[instructions[2]]
    save = instructions[3]
    
    if instructions[0]==1:
        result = x+y
    else:
        result = x*y
    
    op[save] = result
    
    i +=4

print(op[0])

#####################################
#Part 2

def noun_verb(original_data):
    
    
    for i in range(99):
                
        for j in range(99):
            
            amended_data = copy.deepcopy(original_data)
            
            amended_data[1] = i
            amended_data[2] = j
            
            n = 0
            
            while True:
    
                if amended_data[n] == 99:
                    break
            
                instructions = amended_data[n:n+4]
                
                x = amended_data[instructions[1]]
                y = amended_data[instructions[2]]
                save = instructions[3]
                
                if instructions[0]==1:
                    result = x+y
                else:
                    result = x*y
                
                amended_data[save] = result
                
                n +=4
                
            if amended_data[0] == 19690720:
                return i, j
        

noun, verb = noun_verb(content)
print(100*noun + verb)
