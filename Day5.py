import IntCodeFcts as ICF
import copy

f = open('Day5.txt', 'r')
intcode = (f.read()).split(',')
f.close()
intcode = [int(i) for i in intcode]

original = copy.deepcopy(intcode)

code_input = 1

i = 0
while True:
    opcode = intcode[i]     
    if opcode == 99:
        break
   
    if len(str(opcode)) > 1 and opcode % 10 != 4:
        code_block = ICF.manipulate_instruction(instruction = intcode[i: i + 4],
                                                data = intcode,
                                                n = i)  
    elif len(str(opcode)) > 1 and opcode % 10 == 4:
        code_block = [4,0]
    else:
        n = ICF.block_length(opcode)
        code_block = intcode[i: i + n]
        
    print(code_block)
    opcode = code_block[0]
    
    if opcode == 1:
        ICF.opcode_1(instruction = code_block, data = intcode)
        i_length = 4
        
    elif opcode == 2:
        ICF.opcode_2(instruction = code_block, data = intcode)
        i_length = 4
    
    elif opcode == 3: #or opcode == 4:
        ICF.opcode_3(inp = code_input, instruction = code_block, data = intcode)
        i_length = 2
    
    elif opcode == 4:
        ICF.opcode_4(instruction = code_block, data = intcode)
        i_length = 2
    
    i += i_length
    
    
    
######## Part 2 ###############
    
code_input = 5

i = 0
while True:
    opcode = intcode[i]
    #print('original block: ', intcode[i: i + 4])
         
    if opcode == 99:
        break
   
    if len(str(opcode)) > 1 and opcode % 10 != 4:
        code_block = ICF.manipulate_instruction(instruction = intcode[i: i + 4],
                                                data = intcode,
                                                n = i)  
    elif len(str(opcode)) > 1 and opcode % 10 == 4:
        code_block = [4, 0]
    else:
        n = ICF.block_length(opcode)
        code_block = intcode[i: i + n]
        
   # print('edited code block: ', code_block)
    opcode = code_block[0]
    
    if opcode == 1:
        ICF.opcode_1(instruction = code_block, data = intcode)
        i_length = 4
        
    elif opcode == 2:
        ICF.opcode_2(instruction = code_block, data = intcode)
        i_length = 4
    
    elif opcode == 3: #or opcode == 4:
        ICF.opcode_3(inp = code_input, instruction = code_block, data = intcode)
        i_length = 2
    
    elif opcode == 4:
        ICF.opcode_4(instruction = code_block, data = intcode)
        i_length = 2
    
    elif opcode == 7:
        ICF.opcode_7(instruction = code_block, data = intcode)
        i_length = 4
        
    elif opcode == 8:
        ICF.opcode_8(instruction = code_block, data = intcode)
        i_length = 4
    
    if opcode == 5:
        m = ICF.opcode_5(instruction = code_block, data = intcode)
        i_length = 3
    elif opcode == 6:
        m = ICF.opcode_6(instruction = code_block, data = intcode)
        i_length = 3
    else:
        m = None
        
    if m != None:
        i = intcode[m]
    else:
    
        i += i_length
