#c="C:\\Users\\user\\Desktop\\Documentos\\"

def waiting_response():
        print("")
        input("teclee una tecla para continuar...")

c= "C:\\Users\\Colibecas\\optativa_PLN\\"
e="Informacion_del_ordenador_PLN.txt"
s="archivo_nuevo.txt"
e2=open(c+e,"r")
#print(e2.read())
s2=open(c+s,"w")
t=e2.read()
t2=t
s2.write(t2)
e2.close()
s2.close()
#s3=open(c+s,"r")
#print(s3.read())
with open(c+s,"r") as archivo:
    texto=archivo.read()
palabra = input("Escribe la palabra a buscar:   ")
print(texto)

if palabra in texto:
    print("Encontré la palabra")
else:
    print("no encontré la palabra")
#s3.close()