import re 
import math

all_games = open("input.txt", "r")

game_trials = []
wins_trials = []

for line in all_games:
    line = line.split(':')
    line = line[1].split('|')

    trial = re.findall(r'\d+', line[1])
    game_trials.append(trial)

    wins = re.findall(r'\d+', line[0])
    wins_trials.append(wins)

total = 0

index = 0
for game in game_trials: 
    count = 0
    for card in game:
        if card in wins_trials[index]:
            count=count+1
    if count>=1:
        total+=math.pow(2, count-1) 
    index+=1

print(total) 


