# Haciendo uso del debugger, corrige los errores sintácticos del siguiente programa:
def ejercicio1bis():
    password = input("Introduce la contraseña: ")           #las comillas estan mal puestas
    if password in ("sesamo"):                              #igual , estan mal las comillas y poner la palabra entre parentesis
        print('Pasa')
    else:                                                    #faltan cerrar bien el else:
        print('No pasa')



#Ejercicio3
def aplica_iva(base):     # el primer error es que aplica_iva no esta definido, al ser secuencial aun no ha leido el def aplica iva, solucion poner el def primero.
    iva = 1.21
    base = int(base) / iva               #segundo error es que nos dice que iva no esta definido, para arreglarlo añadimos el iva = 21 dentro de la funcion
                                        #tercer error es que al introducir la base, es un str, por lo tanto para multiplicarlo por el iva hay que pasarlo a int
                                        #el iva en este caso no es 21, ese seria el porcentaje, para que sea correto se debe poner 1.21 , y la formula seria base/1.21
    return base
# base = input("Introduce la base imponible de la factura: ")
# print(aplica_iva(base))

#Ejercicio4

u = (1, 2, 3)
v = (4, 5, 6)
def producto_escalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)
print(producto_escalar(u, v))

#el primer error lo da en la linea 27 indicando que tupla no soporta esos item
