datos = ""
nombreAmigos = []
while datos != " ":
    print("introduzca el nombre de sus amigos")
    datos = input()
    nombreAmigos.append(datos)
nombreAmigos.remove(datos)
for amigos in nombreAmigos:
    print("el nombre de tus amigos es: " + amigos)
    
print("fin del programa")