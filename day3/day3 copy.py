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
    for y in range(len(matrix[x])):
        if matrix[x][y]=="*":

            number_voisin = 0
            numbers=[]


            #gauche
            if y>0:
                if matrix[x][y-1].isnumeric():
                    numbers.append(0)
                    number_length = 1
                    number_y = y-1
                    while matrix[x][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number

            #droite
            if y+1<len(matrix[x]):
                if matrix[x][y+1].isnumeric():
                    numbers.append(0)
                    number_length = 1
                    number_y = y+1
                    while matrix[x][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number

            #au dessus
            if x>0:
                if(matrix[x-1][y].isnumeric()):
                    numbers.append(0)
                    number_length = 1
                    number_y = y
                    while matrix[x-1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    while matrix[x-1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x-1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                elif (y>0) & (y+1<len(matrix[x])) & (matrix[x-1][y-1].isnumeric()) & (matrix[x-1][y+1].isnumeric()):
                    #gauche
                    numbers.append(0)
                    number_length = 1
                    number_y = y-1
                    while matrix[x-1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x-1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number

                    #droite
                    numbers.append(0)
                    number_length = 1
                    number_y = y+1
                    while matrix[x-1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x-1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                elif (y>0) & (matrix[x-1][y-1].isnumeric()):
                    #gauche
                    numbers.append(0)
                    number_length = 1
                    number_y = y-1
                    while matrix[x-1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x-1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                    print("zone")

                elif (y+1<len(matrix[x])) & (matrix[x-1][y+1].isnumeric()):
 
                    #droite
                    numbers.append(0)
                    number_length = 1
                    number_y = y+1
                    while matrix[x-1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x-1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                    print("zone")
                      
            #en dessous
            if x<len(matrix)-1:
                if(matrix[x+1][y].isnumeric()):
                    numbers.append(0)
                    number_length = 1
                    number_y = y
                    while matrix[x+1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    while matrix[x+1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x+1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                elif (y>0) & (y+1<len(matrix[x])) & (matrix[x+1][y-1].isnumeric()) & (matrix[x+1][y+1].isnumeric()):
                    #gauche
                    numbers.append(0)
                    number_length = 1
                    number_y = y-1
                    while matrix[x+1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x+1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number

                    #droite
                    numbers.append(0)
                    number_length = 1
                    number_y = y+1
                    while matrix[x+1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x+1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                    print("zone")
                elif (y>0) & (matrix[x+1][y-1].isnumeric()):
                    #gauche
                    numbers.append(0)
                    number_length = 1
                    number_y = y-1
                    while matrix[x+1][number_y-1].isnumeric():
                        number_length+=1
                        number_y-=1
                        if number_y==0:
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x+1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                    print("zone")

                elif (y+1<len(matrix[x])) & (matrix[x+1][y+1].isnumeric()):
 
                    #droite
                    numbers.append(0)
                    number_length = 1
                    number_y = y+1
                    while matrix[x+1][number_y+number_length].isnumeric():
                        number_length+=1
                        if number_y+number_length==len(matrix[x]):
                            break
                    number = 0
                    for it in range(number_length):
                        number+= int(matrix[x+1][number_y+it]) * pow(10, number_length-it-1)
                    numbers[-1]=number
                    print("zone")

            if len(numbers)==2:
                ret += numbers[0]*numbers[1]
                print(numbers[0]*numbers[1])
            elif len(numbers)!=2:
                print("test")


print("-------------------------")
print(ret)
