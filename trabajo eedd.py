a=2
b=3
c=3

if c==b:
    print(True)
else:
    print("Tu no esta bueno")

suma=a+b

print(suma)


#Este codigo es de prueba solo para ir tocando cosas.


#Ejercicio3
def aplica_iva(base):     # el primer error es que aplica_iva no esta definido, al ser secuencial aun no ha leido el def aplica iva, solucion poner el def primero.
    iva = 1.21
    base = int(base) / iva               #segundo error es que nos dice que iva no esta definido, para arreglarlo añadimos el iva = 21 dentro de la funcion
                                        #tercer error es que al introducir la base, es un str, por lo tanto para multiplicarlo por el iva hay que pasarlo a int
                                        #el iva en este caso no es 21, ese seria el porcentaje, para que sea correto se debe poner 1.21 , y la formula seria base/1.21
    return base
# base = input("Introduce la base imponible de la factura: ")
# print(aplica_iva(base))