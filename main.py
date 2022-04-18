import FileModifier


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   t=[]
   a=[]
   f= open("categorias.xml")
   l=open("categorias_tratadas.txt", "w")
   f.readline()
   f.readline()
   lines=f.readlines()
   for line in lines:
     t=line.split("/")
     p=t[6].replace("<", "")
     m=p.replace("-", " ")
     y=t[4].replace("-", " ")
     u = t[5].replace("-", " ")
     l.write(y+","+u+","+m+"\n")
     print(y+","+u+","+m+"\n")

   l.close()
   f.close()










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    FileModifier.getcategorias()


