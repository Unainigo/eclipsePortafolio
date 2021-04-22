datos = ""
nombreAmigos = []
while datos != " ":
    print("introduzca el nombre de sus amigos")
    datos = input()
    nombreAmigos.append(datos)
if datos == " ":
    nombreAmigos.remove(datos)
else:
    print("En el array solo hay datos de nombres")
for amigos in nombreAmigos:
    print("el nombre de tus amigos es: " + amigos)
    
print("fin del programa")