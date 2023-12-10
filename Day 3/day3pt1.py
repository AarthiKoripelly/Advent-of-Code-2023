import re
all_symbols = open("input.txt", "r")
# all_symbols = [
# '467..114..',
# '...*......',
# '..35..633.',
# '......#...',
# '617*......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '...$.*....',
# '.664.598..',
# ]

def check_left(symbols, ind, length):
    for _, sym_ind in symbols: 
        if sym_ind == ind-1:
            return True 
    return False

def check_right(symbols, ind, length):
    for _, sym_ind in symbols: 
        if sym_ind == ind+length:
            return True 
    return False 
  
def check_diagonals_above(symbols, ind, length):
    for _, sym_ind in symbols: 
        if ind>=0 and sym_ind >= ind-1 and sym_ind <= ind+length and ind+length<=140:
            return True 
    return False 

def check_diagonals_below(symbols, ind, length):
    for _, sym_ind in symbols: 
        if ind>=0 and sym_ind >= ind-1 and sym_ind <= ind+length and ind+length<=140:
            return True 
    return False  

number_tuples = []
symbol_tuples = [] 

def find_symbols_and_indexes(string):
    string = string.strip()
    pattern = '[^\d\.]'  # Matches any character that is not a digit or a period
    return [(match.group(), match.start()) for match in re.finditer(pattern, string)]

def find_numbers_and_indexes(string):
    string = string.strip()
    pattern = '\d+'
    return [(match.group(), match.start()) for match in re.finditer(pattern, string)]

for line in all_symbols:
    print(len(line))
    number_tuples.append(find_numbers_and_indexes(line))
    symbol_tuples.append(find_symbols_and_indexes(line))

        
total = 0 
for line in range(0, len(number_tuples)): 
    for num, index in number_tuples[line]:
        isBounded = False
        isBounded = isBounded | check_left(symbol_tuples[line], index, len(str(num)))
        isBounded = isBounded | check_right(symbol_tuples[line], index, len(str(num)))
        if line == 0:
            isBounded = isBounded | check_diagonals_below(symbol_tuples[line+1], index, len(str(num)))
        elif line == len(number_tuples)-1:
            isBounded = isBounded | check_diagonals_above(symbol_tuples[line-1], index, len(str(num)))
        else:
            isBounded = isBounded | check_diagonals_below(symbol_tuples[line+1], index, len(str(num)))
            isBounded = isBounded | check_diagonals_above(symbol_tuples[line-1], index, len(str(num)))
        if(isBounded):
            print(int(num))
            total+=int(num)

print(total)
    
    
    

