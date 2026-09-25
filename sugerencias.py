print("===============================\n")   
print("    sugerencias de peliculas \n  ")  
print("===============================\n")
usuario=input("buen dia, cual es tu nombre? ")
print("¿que queres ver hoy, "+usuario+"?") 
peliculas=[["Rapidos y Furiosos","Acción",2001,6.8],["Troya","Acción",2004,7.3],["Terminator 2","Acción",1991,8.6],["¿Y dónde está el piloto?","Comedia",1980,7.7],["Blair Witch","Terror",2016,5.1],["Coco","Animación",2017,8.4],["Toy story","Animación",1995,8.3],["Shrek","Animación",2001,7.9],["El exorcista","Terror",1973,8.1],["¿Y dónde están las rubias?","Comedia",2004,5.8],["Son como niños","Comedia",2010,6]]
print("----GENEROS-----")
print("accion")
print("comedia")
print("animacion")
print("terror")
genero_favorito=input("¿que genero te gusta? ")
rating_favorito=float(input("¿cual es el rating minimo?"))
print("buscando peliculas del genero "+genero_favorito)
encontrar_pelicula=False
# print(peliculas[4][0])
for pelicula in  peliculas:
    nombre= pelicula[0]
    genero= pelicula[1]
    rating=pelicula[3]
    if (genero_favorito==genero) and (rating_favorito<rating):
        print(nombre)
        encontrar_pelicula=True

# if (genero_pelicula==genero_favorito) and (rating_favorito<rating_pelicula):
#     print(nombre_pelicula)
#     encontrar_pelicula=True

# if (genero_pelicula2==genero_favorito) and (rating_favorito<rating_pelicula2):
#     print(nombre_pelicula2) 
#     encontrar_pelicula=True
    
# if (genero_pelicula3==genero_favorito) and (rating_favorito<rating_pelicula3):
#     print(nombre_pelicula3)
#     encontrar_pelicula=True
    
# if (genero_pelicula4==genero_favorito) and (rating_favorito<rating_pelicula4):
#     print(nombre_pelicula4) 
#     encontrar_pelicula=True
    
# if (genero_pelicula5==genero_favorito) and (rating_favorito<rating_pelicula5):
#     print(nombre_pelicula5) 
#     encontrar_pelicula=True
    
# if  (genero_pelicula6==genero_favorito) and (rating_favorito<rating_pelicula6):
#     print(nombre_pelicula6) 
#     encontrar_pelicula=True
       
#     if(genero_pelicula7==genero_favorito) and (rating_favorito<rating_pelicula7):
#        print(nombre_pelicula7)
#        encontrar_pelicula=True

# if  (genero_pelicula8==genero_favorito) and (rating_favorito<rating_pelicula8):
#     print(nombre_pelicula8)
#     encontrar_pelicula=True
# if (not encontrar_pelicula):
# 	print("No se ha encontrado ninguna pelìcula.")


 