import re
game_list = open("input.txt", "r")
games_filled = []

# 12 red cubes, 13 green cubes, and 14 blue cubes

for game in game_list:
    game = game.split(': ')
    split_by_subgame = game[1].split('; ')
    game_round = []

    for split in split_by_subgame:
        subgame = [0,0,0]
        split = split.split(",")
        for sub in split:
            red = re.findall(r'\b\d+\s*red[s]?\b', sub)
            if (red!=[]):
                subgame[0] = re.findall(r'\d+', red[0])[0]
                continue 
            
            blue = re.findall(r'\b\d+\s*blue[s]?\b', sub)
            if (blue!=[]):
                subgame[1] = re.findall(r'\d+', blue[0])[0]
                continue
            
            green = re.findall(r'\b\d+\s*green[s]?\b', sub)
            if (green!=[]):
                subgame[2] = re.findall(r'\d+', green[0])[0]
        game_round.append(subgame)
        #print([game_round])
    games_filled.append([game_round])

total = 0
for round in range(0, len(games_filled)):
    for trial in games_filled[round]: 
        red_val = 0
        blue_val = 0
        green_val = 0
        for game in trial:
            if(int(game[0]) > red_val):
                red_val = int(game[0])
            if(int(game[1]) > blue_val):
                blue_val = int(game[1])
            if(int(game[2]) > green_val):
                green_val = int(game[2])
        total += red_val*blue_val*green_val

print(total)


