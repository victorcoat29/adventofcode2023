# Ouvrir le fichier en lecture seule
file = open('./day6/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 1
time =[]
distance = []
time_split = lines[0][6:].split(" ")
distance_split  = lines[1][9:].split(" ")

first = 0
last = 0

possibilities = []

for it in time_split:
    if it != "":
        time.append(int(it))

for it in distance_split:
    if it != "":
        distance.append(int(it))

for i in range(len(time)):
    for j in range(time[i]):
        travel = j * (time[i] - j)
        if travel > distance[i]:
            first = j
            break

ret = time[0] - first * 2 + 1 

print("-------------------------")
print(ret)
