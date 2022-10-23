

temperaturliste = []

gjenomsnitt = 0

telling = 0

with open ('/Applications/Visual Studio Code/grunnleggende/temperatur.txt', 'rt') as myfile:
    contents = myfile.readlines()

for line in contents:
    temperaturliste.append(int(line.strip()))


for i in range(len(temperaturliste)):
    telling += 1
    gjenomsnitt += temperaturliste[i]



print(gjenomsnitt/telling)


