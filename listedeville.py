from OSMPythonTools.api import Api
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import csv

##https://wiki.openstreetmap.org/wiki/Canada_admin_level
## Ville = admin level 8

provinceQC = 61549 #relation

api = Api()
overpass = Overpass()
quebecQuery = api.query("relation/61549")

query = overpassQueryBuilder(area=quebecQuery, elementType="relation", selector='"admin_level"=8',out="body")
result = overpass.query(query)

test = result.elements()[1000]
print(test.areaId(),test.tag("name"))

output = "listeDeVille.csv"

output = open(output, "x")
output = csv.writer(output)
header = ["nom", "id"]
output.writerow(header)
for ville in result.elements() :
    row = [ville.tag("name"),ville.areaId()]
    print(row)
    output.writerow(row)
