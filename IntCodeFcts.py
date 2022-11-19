def opcode_1(instruction, data):
    x = data[instruction[1]]
    y = data[instruction[2]]
    
    data[instruction[3]] = x + y
    
def opcode_2(instruction, data):    
    x = data[instruction[1]]
    y = data[instruction[2]]
    
    data[instruction[3]] = x * y
    
def opcode_3(inp, instruction, data):
    data[instruction[1]] = inp
    
def opcode_4(instruction, data):
    print(data[instruction[1]])
    
def opcode_5(instruction, data):
    if data[instruction[1]] != 0:
        return instruction[2]
    else:
        return None
    
def opcode_6(instruction, data):
    if data[instruction[1]] == 0:
        return instruction[2]
    else:
        return None
    
def opcode_7(instruction, data):
    if data[instruction[1]] < data[instruction[2]]:
        data[instruction[3]] = 1
    else:
        data[instruction[3]] = 0
        
def opcode_8(instruction, data):
    if data[instruction[1]] == data[instruction[2]]:
        data[instruction[3]] = 1
    else:
        data[instruction[3]] = 0
    

def manipulate_instruction(instruction, data, n):
    param = instruction[0]
    opcode = param % 10
    p1_mode = (param // 100) % 10
    p2_mode = (param // 1000) % 10
    
    if p1_mode == 1:
        p1 = n + 1
    else:
        p1 = instruction[1]
        
    if p2_mode == 1:
        p2 = n + 2
    else:
        p2 = instruction[2]
    
    return [opcode, p1, p2, instruction[3]]

def block_length(op):
    if op == 3 or op == 4:
        return 2
    elif op == 5 or op == 6:
        return 3
    else:
        return 4