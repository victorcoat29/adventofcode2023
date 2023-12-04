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
    for i in range(len(line)):
        chr = line[i]
        if chr.isnumeric():
            last = int(chr)
            if first == -1:
                first = int(chr)

        if line[i:i+3] == "one":
            last = 1
            if first == -1:
                first = 1

        if line[i:i+3] == "two":
            last = 2
            if first == -1:
                first = 2

        if line[i:i+5] == "three":
            last = 3
            if first == -1:
                first = 3

        if line[i:i+4] == "four":
            last = 4
            if first == -1:
                first = 4

        if line[i:i+4] == "five":
            last = 5
            if first == -1:
                first = 5

        if line[i:i+3] == "six":
            last = 6
            if first == -1:
                first = 6

        if line[i:i+5] == "seven":
            last = 7
            if first == -1:
                first = 7

        if line[i:i+5] == "eight":
            last = 8
            if first == -1:
                first = 8

        if line[i:i+4] == "nine":
            last = 9
            if first == -1:
                first = 9

    if (first == -1) or (last == -1):
        print("error")
    else:
        vals.append(10*first+last)
        print(vals[-1])

print(sum)

for val in vals:
    ret+=int(val)
    print(ret)

print("-------------------------")
print(ret)
