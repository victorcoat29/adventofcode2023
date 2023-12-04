# Ouvrir le fichier en lecture seule
file = open('./day2/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 0

min_per_game = []

for i in range(len(lines)):
    max_blue = 0
    max_red = 0
    max_green = 0
    temp = lines[i][:-1].split(":")
    tirages = temp[1].split(";")
    for tirage in tirages:
        cubes = tirage.split(",")
        for cube in cubes:
            cube = cube[1:]
            cube_split = cube.split(" ")
            if cube_split[1] == "red":
                if int(cube_split[0]) > max_red:
                    max_red=int(cube_split[0])
            elif cube_split[1] == "blue":
                if int(cube_split[0]) > max_blue:
                    max_blue=int(cube_split[0])
            elif cube_split[1] == "green":
                if int(cube_split[0]) > max_green:
                    max_green=int(cube_split[0])
    
    min_per_game.append(max_blue*max_green*max_red)

for val in min_per_game:
    ret += val
print("-------------------------")
print(ret)
