import re
string_list = open("input.txt", "r")
string_list_forward = []
string_list_reverse = []

def string_replace_forward(x):
    x = x.replace( 'one', 'o1ne')
    x = x.replace( 'two', 't2wo')
    x = x.replace( 'three', 'th3ree')
    x = x.replace( 'four', 'f4our')
    x = x.replace( 'five', 'f5ive')
    x = x.replace( 'six', 'si6x')
    x = x.replace( 'seven', 'se7ven')
    x = x.replace( 'eight', 'ei8ght')
    x = x.replace( 'nine', 'ni9ne')
    return x 

for string in string_list:
    string = string.strip()
    string_list_forward.append(string_replace_forward(string))

total_sum = 0

for string_for in string_list_forward:
    val_tens = 0
    val_zeros = 0
    for i in string_for: 
        if i.isdigit():
            val_tens = int(i)
            break 
    for i in string_for[::-1]: 
        if i.isdigit():
            val_zeros = int(i)
            break 

    if (val_tens == 0):
        val_tens = val_zeros
    if (val_zeros == 0):
        val_zeros = val_tens
    total_sum += val_tens*10 + val_zeros

print(total_sum)
        
