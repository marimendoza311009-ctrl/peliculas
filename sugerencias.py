print("=============================\n")
print("   Sugerencias de peliculas  \n")
print("=============================\n")
usuario=input("Buen dia, cual es tu nombre? ")
print("¿Que queres ver hoy, "+usuario+"?")
nombre_pelicula="Rapido Furioso"
genero_pelicula="accion"
anio_pelicula=2001
rating_pelicula=6.8
nombre_pelicula2="Troya"
genero_pelicula2="accion"
anio_pelicula2=2004
rating_pelicula2=7.4
nombre_pelicula3="Terminator"
genero_pelicula3="accion"
anio_pelicula3=1984
rating_pelicula3=8.1
nombre_pelicula4="¿Y donde esta el piloto?"
genero_pelicula4="Comedia"
anio_pelicula4=1980
rating_pelicula4=7.7
nombre_pelicula5="Son como niños"
genero_pelicula5="Comedia"
anio_pelicula5=2010 
rating_pelicula5=6
nombre_pelicula6="Spiderman"
genero_pelicula6="accion"
anio_pelicula6=2002
rating_pelicula6=7.4
print("----GENEROS----")
print("ACCION")
print("COMEDIA")
genero_favorito=input("¿Que genero te gusta? ")
print("Buscando peliculas del genero: " +genero_favorito)
if (genero_pelicula==genero_favorito):
    print(nombre_pelicula)
if (genero_pelicula2==genero_favorito):
    print(nombre_pelicula2)
if (genero_pelicula3==genero_favorito):
    print(nombre_pelicula3)
if(genero_pelicula4==genero_favorito):
    print(nombre_pelicula4)
if (genero_pelicula5==genero_favorito):
    print(nombre_pelicula5)
if (genero_pelicula6==genero_favorito):
    print(nombre_pelicula6)    
            
