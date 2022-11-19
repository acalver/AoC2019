count = 0

for n in range(248345, 746316):
    digits = [int(i) for i in str(n)]
    
    if len(set(digits)) < 6 and digits[0] <= digits[1] \
    and digits[1] <= digits[2] and digits[2] <= digits[3] \
    and digits[3] <= digits[4] and digits[4] <= digits[5]:
        count += 1
        
print(count)


#########################
#Part 2

dictionary = {}
counter = 0

for number in range(248345, 746316):
  dictionary = {}
  password = str(number)
  digit = [int(i) for i in password]
  for element in digit:
    if element in dictionary.keys():
      dictionary[element] +=1
    else:
      dictionary[element] = 1
  
  for values in dictionary.values():
    if values == 2:
      if digit[0] <= digit[1] and digit[1] <= digit[2] and \
      digit[2]<= digit[3] and digit[3] <= digit[4] and digit[4] <= digit[5]:
        counter += 1 
        break   
        

print(counter)