from io import open


archivo_texto=open('nombres.txt','r')

#archivo_texto.write('\n datos en el archivo')
#archivo_texto.close()

#volver el cursor a la primera linea
#archivo_texto.seek(0)
for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

archivo_texto.close()