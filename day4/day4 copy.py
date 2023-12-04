# Ouvrir le fichier en lecture seule
file = open('./day4/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 0
streak = []
for i in range(len(lines)):
    streak.append(1)
for i in range(len(lines)):
    card_wins = 0
    winnings = []
    cards = []
    line = lines[i][:-1].split(": ")
    line = line[1].split(" | ")
    winning_str = line[0].split(" ")
    cards_str = line[1].split(" ")
    for it in winning_str:
        if it != "":
            winnings.append(int(it))
    for it in cards_str:
        if it != "":
            cards.append(int(it))
    score = 0
    for card in cards:
        for win in winnings:
            if card == win:
                if score == 0:
                    score = 1
                    card_wins += 1
                else : 
                    score = score * 2
                    card_wins += 1

    for j in range(card_wins):
        if(j < len(lines)):
            streak[i+j+1]+=streak[i]

for i in streak:
    ret += i
print("-------------------------")
print(ret)
