# Ouvrir le fichier en lecture seule
file = open('./day3/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 0

matrix = []
symbols=["*","#","+","$","=","-","/","@","%","&"]

for line in lines:
    matrix.append([])
    for chr in line:
        matrix[-1].append(chr)

for x in range(len(matrix)):
    y=0
    while y < len(matrix[x]):
        number_length=1
        if matrix[x][y].isnumeric():
            while matrix[x][y+number_length].isnumeric():
                number_length+=1
                if y+number_length==len(matrix[x]):
                    break
        else:
            y+=1
            continue

        number = 0
        for it in range(number_length):
            number+= int(matrix[x][y+it]) * pow(10, number_length-it-1)
        
        is_valid=False
        #au dessus
        if x>1:
            for it in range(number_length):
                if matrix[x-1][y+it] in symbols:
                    is_valid = True
            
        #gauche
        if y>1:
            if x>1:
                if matrix[x-1][y-1] in symbols:
                    is_valid = True
            if x<len(matrix)-1:
                if matrix[x+1][y-1] in symbols:
                    is_valid = True
            if matrix[x][y-1] in symbols:
                    is_valid = True

        #droite
        if y+number_length<len(matrix[x]):
            if x>1:
                if matrix[x-1][y+number_length] in symbols:
                    is_valid = True
            if x<len(matrix)-1:
                if matrix[x+1][y+number_length] in symbols:
                    is_valid = True
            if matrix[x][y+number_length] in symbols:
                    is_valid = True

        #en dessous
        if x<len(matrix)-1:
            for it in range(number_length):
                if matrix[x+1][y+it] in symbols:
                    is_valid = True

        if is_valid:
            ret += number
            print(number)

        #further            
        y+=number_length


print("-------------------------")
print(ret)
