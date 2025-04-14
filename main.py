from OSMPythonTools.api import Api
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import csv

extra =3600000000

listVille = []
villeSource = "combo.csv"
villeSource = open(villeSource, "r")
villeSource = csv.reader(villeSource)

##convert csv to list of lists


##apicall
global api
global overpass
global queryElements
api = Api()
overpass = Overpass()
queryElements = ["bar","restaurant","pub"]

def apiCall(villeID):
    queryarea = api.query("relation/"+str(villeID))
    resultatsList = []
    for x in queryElements:
        selector = '"amenity"='+'"'+x+'"'
        query = overpassQueryBuilder(area=queryarea, elementType="node", selector=selector,out="body")
        results = overpass.query(query)
        for result in results.elements() :
            establishment = {"name":result.tag("name"),
                             "type":result.tag("amenity")}
            resultatsList.append(establishment)
    return(resultatsList)



outputFile = "barOutput.csv"
outputFile = open(outputFile, "w")
outputFile = csv.writer(outputFile)

next(villeSource)
for row in villeSource:
    actualId = row[1] = int(row[1])-extra
    print(row[0])
    listedetablissements = apiCall(row[1])
    row.append(len(listedetablissements))
    row.append(listedetablissements)
    print(row)
    outputFile.writerow(row)
