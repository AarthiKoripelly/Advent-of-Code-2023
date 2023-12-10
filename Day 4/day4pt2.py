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

scratchcards = []
for i in range(0,len(game_trials)):
    scratchcards.append(1)

index = 0
for game in game_trials: 
    count = 0
    for card in game:
        if card in wins_trials[index]:
            count=count+1
    val = scratchcards[index]
    for i in range(0,count):
        if index+i+1<len(game_trials):
            scratchcards[index+i+1]+=val
    print(scratchcards)
    index+=1

print(sum(scratchcards))


