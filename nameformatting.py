from csvFormatting.formatting import nameCleaner
import csv

sourceName = "ressources/MUN.csv"

listeDeVilles = []
sourceF = open(sourceName,"r")
sourceF = csv.reader(sourceF)
outputF = open("ressources/outputMUN.csv", "w")
outputF = csv.writer(outputF)


for x in sourceF:
    cleanname = nameCleaner(x[1])
    x.append(cleanname)
    outputF.writerow(x)



