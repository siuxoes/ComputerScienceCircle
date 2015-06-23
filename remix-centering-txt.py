__author__ = 'Siuxoes'

width = int(input())
text = input()
while text != 'END':
    longitud = width - len(text)
    if longitud % 2 == 0:
        izquierda = int(longitud / 2)
        derecha = int(longitud / 2)
    else:
        izquierda = int(longitud / 2) + 1
        derecha = int(longitud / 2)
    puntosIzquierda = "." * izquierda
    puntosDerecha = "." * derecha
    print(str(puntosIzquierda) + text + str(puntosDerecha))
    text = input()