# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#%%
print("hola mundo python")




#%%
message = "hola mundo"
print(message)
#%%
"""strings"""
name = "pamela mondragon"
print (name.title())
# comentario .title() string como titulo se ponen mayusculas en las primeras letras
print(name.upper())
#.upper() todo en mayusculas

letra = "RAZON"
print(letra.lower())
#.lowe() todo en minusculas

print(name.capitalize())
#.capitalize() en mayusculas la primera letra de la cadena
#%%


name = "pamela mondragon" 
print(name)
name = "otro nombre"
print(name)
print(name.lower())
#%%
"""combinando strings"""
#guardar el apellido y nombre de otro participante en experimento el + es para combinar als cadenas
first_name = "laura"
last_name = "rivera"
full_name = first_name + " " + last_name
#espacio entre los nombres agregar un +
print(full_name.title())
print("hola "+full_name.title()+"!")
message= "nombre completo de participante: "
print(message + full_name.title())
#%%
#flotantes son decimales en caso de hacer alguna operacion
edad=22
print("la edad promedio de aqui es "+str(edad)+" anios")
#primero ocnvertir el numero en una cadena con str()
#%%
a = 5
b = 2
#%% booleanos
#se hacen comparaciones con los booleanos
a = 5
b = 2

a == b #si son iguales
a != b #si son diferentes

#&&


c = 5
d = 2

c == d
c != d
#%% 

a = True
b= False
c = True

a&b
#%%
meses = ["enero", "febrero", "marzo", "abril", "mayo"]
#cuenta la lista a partir de 0
meses[4] #valor 4 de la lista
meses [0] #primer valor de la lista
#%%
print(meses[-1])
print(meses[-2])
#%%
meses = ["enero", "febrero", "marzo", "abril", "mayo"]
meses[0:2]
meses[1:4]
#%%
meses = ["enero", "febrero", "marzo", "abril", "mayo"]
print(meses)

meses.append("junio")
print(meses)

meses.insert(0,"meses:")
print(meses)

meses.remove("meses:")

print(meses)
#%%
meses = ["enero", "enero", "febrero", "marzo", "abril", "mayo"]
del meses[0:3]

print(meses)
#%%
motorcycles = ["honda", "yamaha", "ducati", "suzuki"]
last_motorcycles = motorcycles.pop()
print("mi ultima moto fue una " + last_motorcycle.title())
#%%
motorcycles = ["honda", "yamaha", "ducati", "suzuki"]
too_expensive = motorcycles.pop(1)
print("la marca mas cara es "+too_expensive)
print(motorcycles)
print(too_expensive)

#%%
magos = ["uriel", "felisa", "jose", "mauricio", "karina", "arturo"]

for mago in magos:
  print(mago.title())
#%%
magos = ["uriel", "felisa", "jose", "mauricio", "karina", "arturo"]
for mago in  magos:
  print("\nEste fue un gran truco "+mago.title()+"!")
  print("no puedo esperar "+mago.title()+ " a ver el siguiente show!")

print("\nEspero verlos pronto a todos!")
#%%
As = [1,2,3,4,5]
for a in As:
  print(a)
#%%

for value in range(1,6):
  print(value)

#%%

numbers = list(range(1,10))

for number in numbers:
  print("el numero es "+str(number))

#%%
even_numbers = list(range(2,11,2))
for even_number in even_numbers:
  print(even_number)

#%%

a = [1,2,3,4,5,6,7]
#%%
import numpy
a = [1,2,3,4,5,6,7]
b = numpy.array(a)
b+1
b*2
#cada elemento se va leer como un arreglo
#%%
def saludo_usuario():
  print("hola!")
  
#%%
def saludo_usuario(usuario):
  print("hola, "+usuario.title()+"!")
#%%
def describe_mascota(name,tipo):
  print("mi mascota se llama "+name" y es un "+tipo)
#%%
magicians = ["uriel", "felisa", "jose"]

def show_magician(magics):
  print("estos son los magos: ")
  for magic in magics:
    print("\n"+magic.title())
    print("\nSon muy guapos") 

#%%



