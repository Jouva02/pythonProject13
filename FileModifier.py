


def getURLS():
    fread = open("categorias.xml", "r", encoding="utf-8")
    fwrite = open("URLcategorias.txt","w",)



    for line in fread.readlines():
        startindex = line.find("<loc>")
        endindex = line.find("</loc>",startindex+5)
        if startindex > 0:
            fwrite.write(line[startindex+5:endindex]+"\n")







