from .chars import acceptedChars

# villes = ["Lac-Akonapwehikan",'ᓀᒥᔅᑳᐤokay (ᐅᑌᓈᐤ) / Nemaska (village)']  ##test list

#### csv unwrapper


def nameCleaner(string2clean :str) -> str:
    return(justeLettres(parentheseQuiFontChier(slashQuiFontChier(string2clean)),string2clean))



def slashQuiFontChier(villeParen):
    villeParen = villeParen.lower()
    strArray = []
    ##remove before /
    try:
        villeParen.index("/")
        slashPos = villeParen.find("/")
        pos = 0
        for char in villeParen:
            if pos > slashPos:
                strArray.append(char)
            pos +=1
        villeParen ="".join(strArray)
        return(villeParen)
    except ValueError:
        return(villeParen)


def parentheseQuiFontChier(villeParen):     ##et parenthèses
    strArray = []
    try:
        villeParen.index("(")
    except ValueError:
        return(villeParen)
    else :
        ouvertePos = villeParen.find('(')
        fermeePos = villeParen.find(')') 
        delRange = range(ouvertePos,fermeePos+1)
        pos = 0
        for char in villeParen:
            if pos not in delRange:
                strArray.append(char)
            pos +=1
        villeParen ="".join(strArray)
        return(villeParen)

##charreplacement
global forbidenDict
e = ["é","è","ë","ê"]
o = ["ô"]
i = ["î","ï"]
a = ["à","â"]
c = ["ç"]
oe = ["œ"]
blank = ["-"," ","'",":","–","ᑲ","ᐛ","ᐛ","ᒋ","ᒡ","!","ᒪ","ᐳ","ᕕ","ᕐ","ᓂ","ᑐ","ᖅ","1","2","3","4","5","6","7","8","9","0"]
forbidenDict = {"e":e,
                "o":o,
                "i":i,
                "a":a,
                "c":c,
                "oe":oe,
                "":blank}

def justeLettres(ville,og):
    ville = ville.lower()
    strArray = []
    for char in ville:
        replaced = False
        if char in acceptedChars:
            strArray.append(char)
        else :
            for k, v in forbidenDict.items():
            # print(k,v)
                if char in v:
                    newchar = k
                    strArray.append(newchar)
                    replaced = True
            if replaced == False :
                raise Exception("New char : "+"'"+char+"'"+" in "+ og)
    nomFormatte = "".join(strArray)
    return(nomFormatte)


# for ville in villes:
#     print("******")
#     villeSansslash = slashQuiFontChier(ville)
#     print("/",villeSansslash)
#     villeSansParen = parentheseQuiFontChier(villeSansslash)
#     print("()",villeSansParen)
#     villeLettres = justeLettres(villeSansParen)
#     print("&*",villeLettres)