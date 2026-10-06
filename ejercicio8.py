nombre = input("¿Cuál es tu nombre ?")
edad = int(input("¿Cuál es tu edad ?"))
calificacion1 = float(input("¿Cuál es tu primera calificacion ?"))
calificacion2 = float(input("¿Cuál es tu segunda calificacion ?"))
calificacion3 = float(input("¿Cuál es tu tercera calificacion ?"))

promedio = (calificacion1 + calificacion2 + calificacion3) /3

if promedio >= 71:
    print("Hola", nombre, "estas ¡Aprobado! ")
else:
    print("Hola", nombre ,"estas ¡Reprobado! ")
    
