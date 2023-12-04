# Ouvrir le fichier en lecture seule
file = open('./day2/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 0

max_blue = 14
max_red = 12
max_green = 13

for i in range(len(lines)):
    game_id = i+1
    game_isOk = True
    temp = lines[i].split(":")
    tirages = temp[1].split(";")
    for tirage in tirages:
        cubes = tirage.split(",")
        for cube in cubes:
            cube = cube[1:]
            cube_split = cube.split(" ")
            if cube_split[1] == "red":
                if int(cube_split[0]) > max_red:
                    game_isOk = False
            elif cube_split[1] == "blue":
                if int(cube_split[0]) >max_blue:
                    game_isOk = False
            elif cube_split[1] == "green":
                if int(cube_split[0]) >max_green:
                    game_isOk = False
    
    if game_isOk:
        ret+=game_id


print("-------------------------")
print(ret)
