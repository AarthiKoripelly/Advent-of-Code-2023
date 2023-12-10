import re
all_symbols = open("input.txt", "r")
# all_symbols = [
# '..224.....487...................718.....................378............................................284........310......313..........311.',
# '....*..............................*744....486*485......*......741......@...359.#666...439................*925....*......$..+........@......',
# '.235................758..440...........................251....*......262.....*..........*......................752......774.......515.......']


def check_right(numbers, sym_ind):
    for num, num_ind in numbers: 
        if sym_ind == num_ind-1:
            return num 
    return 

def check_left(numbers, sym_ind):
    for num, num_ind in numbers: 
        if sym_ind == num_ind+len(str(num)):
            return num 
    return  
  
def check_diagonals_above(numbers, sym_ind):
    all = []
    for num, ind in numbers: 
        if ind>=0 and sym_ind >= ind-1 and sym_ind <= ind+len(str(num)) and ind+len(str(num)) <=140:
            all.append(num) 
    return all 

def check_diagonals_below(numbers, sym_ind):
    all = []
    for num, ind in numbers: 
        if ind>=0 and sym_ind >= ind-1 and sym_ind <= ind+len(str(num)) and ind+len(str(num)) <=140:
            all.append(num) 
    return all 

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
    number_tuples.append(find_numbers_and_indexes(line))
    symbol_tuples.append(find_symbols_and_indexes(line))

        
total = 0 
for line in range(0, len(number_tuples)): 
    for sym, index in symbol_tuples[line]:
        if sym=='*':
            gears = []
            gears.append(check_left(number_tuples[line], index))
            if gears[0]==None:
                gears.pop()
            gears.append(check_right(number_tuples[line], index))
            if gears[0]==None:
                gears.pop()
            if line == 0:
                nums = check_diagonals_below(number_tuples[line+1], index)
                for i in nums:
                    if i != None: 
                        gears.append(i)
            elif line == len(number_tuples)-1:
                nums = check_diagonals_above(number_tuples[line-1], index)
                for i in nums:
                    if i != None: 
                        gears.append(i)
            else:
                nums = check_diagonals_below(number_tuples[line+1], index)
                for i in nums:
                    if i != None: 
                        gears.append(i)
                nums = check_diagonals_above(number_tuples[line-1], index)
                for i in nums:
                    if i != None: 
                        gears.append(i)
            
            gears_no_none = []
            for i in gears:
                if i!=None:
                    gears_no_none.append(i)
            
            if(len(gears_no_none)==2):
                total+=int(gears_no_none[0])*int(gears_no_none[1])

print(total)
    
    
    

