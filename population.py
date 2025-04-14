from bs4 import BeautifulSoup
import csv
sourcefile = "ressources/A01_CONVERT_XML_POP.xml"
sourcefile = open(sourcefile, "r")
soup = BeautifulSoup(sourcefile,"xml")
item = soup.find_all('population')

listoflist = []
for x in item :
    locallist = []
    pop = x.find('POP')
    tag = x.find('COD_GEO_N')
    locallist = pop.string, tag.string
    listoflist.append(locallist)

outputfile = "pop.csv"
outputfile = open(outputfile,"a")
fieldnames = ['population','COD_GEO_N']
outputcsv = csv.writer(outputfile)
outputcsv.writerow(fieldnames)
outputcsv.writerows(listoflist)

