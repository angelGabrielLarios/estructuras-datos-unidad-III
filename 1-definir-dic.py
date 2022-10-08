print('')

dic1 = {
    "Libro" : "Al servicio de su majestad",
    "Autor" : "Gordon Thomas",
    "ISBN" : 43500
}

print(dic1)
print('')

""" definir un constructor con dict """


dic2 = dict(
    [
        ("Libro", "Mexicanas que hicieron historia"),
        ("Autor", "Pedro J. Fernandez"),
        ("ISBN", 604)
    ]
)

print(dic2)
print('')

""" otra forma de definir un diccionario dict """

dic3 = dict(
    Libro="Harry Potter and the Globet of fire",
    Autor="J.K. Rowling",
    ISBN=29917
)

print(dic3)
print('')

""" Acceso a las llaves de un diccionario """
print(dic1["Autor"])
print('')
print(dic2.get('Libro'))
print('')


""" modificar el valor del diccionario """
dic2['ISBN'] = 978
print(dic2)
print('')


""" añadir elementos """


dic3['Editorial'] = 'Schoñastic'
print(dic3)
print('')

dic2['Editorial'] = 'Alfaguara'
print(dic3)
print('')


dic1['Editorial'] = 'Ediciones B'
print(dic3)
print('')



""" iterar diccionarios """

""" imprimir llaves """
for key in dic1:
    print(key)

print('')

""" imprimir values """
for key in dic1:
    print(dic1[key])

print('')

""" imprimir  key y value """
for x, y in dic2.items():
    print(x, y)
print('')



for key in dic2:
    valor = dic2[key]
    print(f'{key} -> {valor}')
