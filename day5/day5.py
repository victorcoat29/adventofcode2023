# Ouvrir le fichier en lecture seule
file = open('./day5/input.txt', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes

ret = 0
seeds = []
soil_conv = []
fertilizer_conv = []
water_conv = []
ligth_conv = []
temperature_conv = []
humidity_conv = []
location_conv = []
location=[]

iterator = 0

for line in lines:
    if line.find("seeds: ") == 0:
        seeds = line[7:-1].split(" ")    
    elif line == "\n":
        iterator+=1
    elif line[0].isnumeric() == True:
        if iterator == 1:
            soil_conv.append(line[:-1].split(" "))
        elif iterator == 2:
            fertilizer_conv.append(line[:-1].split(" "))
        elif iterator == 3:
             water_conv.append(line[:-1].split(" "))
        elif iterator == 4:
             ligth_conv.append(line[:-1].split(" "))
        elif iterator == 5:
             temperature_conv.append(line[:-1].split(" "))
        elif iterator == 6:
             humidity_conv.append(line[:-1].split(" "))
        elif iterator == 7:
             location_conv.append(line[:-1].split(" "))
            
for it in range(len(soil_conv)):
    for it2 in range(len(soil_conv[it])) :
        soil_conv[it][it2] = int(soil_conv[it][it2])

for it in range(len(fertilizer_conv)):
    for it2 in range(len(fertilizer_conv[it])) :    
        fertilizer_conv[it][it2] = int(fertilizer_conv[it][it2])

for it in range(len(water_conv)):
    for it2 in range(len(water_conv[it])) :    
        water_conv[it][it2] = int(water_conv[it][it2])

for it in range(len(ligth_conv)):
    for it2 in range(len(ligth_conv[it])) :    
        ligth_conv[it][it2] = int(ligth_conv[it][it2])

for it in range(len(temperature_conv)):
    for it2 in range(len(temperature_conv[it])) :    
        temperature_conv[it][it2] = int(temperature_conv[it][it2])

for it in range(len(humidity_conv)):
    for it2 in range(len(humidity_conv[it])) :    
        humidity_conv[it][it2] = int(humidity_conv[it][it2])

for it in range(len(location_conv)):
    for it2 in range(len(location_conv[it])) :    
        location_conv[it][it2] = int(location_conv[it][it2])

def seed_to_soil(entree):
    sortie = entree
    for it in soil_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def soil_to_fertilizer(entree):
    sortie = entree
    for it in fertilizer_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def fertilizer_to_water(entree):
    sortie = entree
    for it in water_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def water_to_ligth(entree):
    sortie = entree
    for it in ligth_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def ligth_to_temperature(entree):
    sortie = entree
    for it in temperature_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def temperature_to_humidity(entree):
    sortie = entree
    for it in humidity_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)

def humidity_to_location(entree):
    sortie = entree
    for it in location_conv:
        if (entree >= it[1]) & (entree < it[1] + it[2]):
            return(it[0] + entree - it[1])
    return(sortie)



for seed in seeds:
    seed = int(seed)
    soil = seed_to_soil(seed)
    ferti = soil_to_fertilizer(soil)
    water = fertilizer_to_water(ferti)
    ligth = water_to_ligth(water)
    temp = ligth_to_temperature(ligth)
    humi = temperature_to_humidity(temp)
    location.append(humidity_to_location(humi))
    print(location[-1])

print("-------------------------")
ret = location[0]
for it in location:
    if it < ret :
        ret = it
print(ret)
