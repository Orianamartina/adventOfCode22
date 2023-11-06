"""
A   rock      X   1 p.
B   paper     Y   2 p.
C   scissors  Z   3 p.

"""


scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "draw": 3,
    "loose": 0
}

with open("day2/2input.txt", "r") as file:
    file_contents = file.read()

rounds = file_contents.split('\n')

#El número de la derecha le gana al número a su izquierda
figureScores =[3,1,2,3,1]

def winningCondition(opponent, player):
   """ return(
        (opponent == 1 and player == 2) or (opponent == 2 and player ==3) or (opponent == 3 and player == 1)
    )"""
   return(
       figureScores[player] == (figureScores[opponent + 1])
   )


score = 0
for round in rounds:
    opponent = round[0]
    player = round[2]
    if scores[opponent] == scores[player]:
        score += scores["draw"]
    elif winningCondition(scores[opponent], scores[player]):
        score += scores["win"]
    else:
        score += scores["loose"]
    score += scores[player]

print (f'Answer to puzzle 2.1: {score}')


score = 0
for round in rounds:
    opponent = round[0]
    player = round[2]
    if scores[player] == 1:
        score += figureScores[scores[opponent]-1]
    elif scores[player] == 2:
        score += figureScores[scores[opponent]] + scores["draw"]
    else:
        score += figureScores[scores[opponent]+1] + scores["win"]

print(f'Answer to puzzle 2.2: {score}')
