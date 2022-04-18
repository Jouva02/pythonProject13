




def getURLS():
    fread = open("categorias.xml", "r", encoding="utf-8")
    fwrite = open("URLcategorias.txt","w",)



    for line in fread.readlines():
        startindex = line.find("<loc>")
        endindex = line.find("</loc>",startindex+5)
        if startindex > 0:
            fwrite.write(line[startindex+5:endindex]+"\n")




def getcategorias():
    fread = open("URLcategorias.txt", "r", encoding="utf-8")
    fwrite = open("categorias_tratadas_monte.txt","w",)

    for line in fread.readlines():
        array = line.split('/')
        categorias = array[4:len(array)]
        for subcategoria in categorias:
            if subcategoria.find('\n') < 0:
                fwrite.write(f"{subcategoria},")
            else:
                fwrite.write(subcategoria)

