# Ouvrir le fichier en lecture seule
file = open('./day1/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

vals = []
ret = 0
first=-1
last=-1

for line in lines:
    first=-1
    last=-1
    for chr in line:
        if chr.isnumeric():
            last = int(chr)
            if first == -1:
                first = int(chr)

    if (first == -1) or (last == -1):
        print("error")
    else:
        vals.append(10*first+last)
        print(vals[-1])

print(sum)

for val in vals:
    ret+=int(val)

print("-------------------------")
print(ret)
