#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

# ============================================================
# Videoclub
# ============================================================
# Programa
# ============================================================

# from fecha import Fecha, lee_fecha
import time
from datetime import date

# Variable de temps
today = date.today()

#-------------------------------------------------------------
# Socio
#-------------------------------------------------------------
# Clase para almacenar los datos relativos a un socio
#-------------------------------------------------------------
class Socio:
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def __str__(self):
        return 'DNI: {0}\nNombre: {1}\nTelefono: {2}\Domicilio: {3}\n' \
            .format(self.dni, self.nombre, self.telefono, self.domicilio)

#-------------------------------------------------------------
# Pelicula
#-------------------------------------------------------------
# Clase para almacenar los datos relativos a un ejemplar de
# una pelicula
#-------------------------------------------------------------
class Pelicula:
    def __init__(self, titulo, genero, dias_permitidos):
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None
        self.fecha_alquiler = None
        self.dias_permitidos = dias_permitidos

    def __str__(self):
        cadena = 'Titulo: {0}\nGenero: {1}\n'.format(self.titulo, self.genero)
        if self.alquilada == None:
            cadena = cadena + 'Disponible\n'
        else:
            cadena = cadena + 'Alquilada a: {0}\n'.format(self.alquilada)
        return cadena
    
#-------------------------------------------------------------
# Videoclub
#-------------------------------------------------------------
# Almacena dos listas: una de socios y otra de peliculas.
# Los elementos de la primera lista son de la clase Socio,
# y los de la segunda, de la clase Pelicula.
#-------------------------------------------------------------
class Videoclub:
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def contiene_socio(self, dni):
        # Devuelve True si existe algun socio con DNI dni y
        # False en caso contrario.
        for socio in self.socios:
            if socio.dni == dni:
                return True
            return False

    def contiene_pelicula(self, titulo):
            # Devuele True si existe alguna pelicula del titulo que nos
            # pasan y False en caso contrario.
            for pelicula in self.peliculas:
                 if pelicula.titulo == titulo:
                     return True
                 return False

    def alta_socio(self, socio):
        # A�ade un socio a la lista de socios.
        # Requisito: no debe existir socio con el mismo DNI.
        self.socios.append(socio)

    def baja_socio(self, dni):
        # Elimina al socio cuyo DNI es igual a dni.
        # Requisito: debe existir un socio con ese DNI.
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break

    def alta_pelicula(self, pelicula, ejemplares):
        # Da de alta un numero dado de ejemplares de una pelicula.
        for i in range(ejemplares):
                nuevo_ejemplar = Pelicula(pelicula.titulo, pelicula.genero, \
                                          pelicula.dias_permitidos)
                self.peliculas.append(nuevo_ejemplar)

    def baja_pelicula(self, titulo, ejemplares):
        # Da de baja un numero de jemplares de la pelicula cuyo titulo nos
        # suministran como argumento. Devuelve el numero de ejemplares que
        # se dio de baja efectivamente.
        bajas_efectivas = 0 
        i = 0
        while i < len(self.peliculas) and bajas_efectivas < ejemplares:
            if self.peliculas[i].titulo == titulo and self.peliculas[i].alquilada == None:
                del self.peliculas[i]
                bajas_efectivas += 1
            else:
                i += 1
        return bajas_efectivas

    def alquilar_pelicula(self, titulo, dni):
        # Alquila un ejemplar de la pleicula cuyo titulo nos indican, al socio
        # con DNI dni. Si no consigue efectuar el alquiler, devuelve False, y True
        # si lo consigue. La fecha de alquiler se fija autom�ticament al dia
        # actual.
        # Requisito: debe existir un socio con el DNI suministrado.
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni
                pelicula.fecha_alquiler = hoy
                return True
            return False

    def devolver_pelicula(self, titulo, dni):
        # Devuelve un ejemplar de la pelicula cuyo titulo nos indican que
        # estaba alquilada al socio con DNI dni. Devuelve el numero de dias
        # de retrase, o -1 si ningun ejemplar de la plicula est� alquilado
        # al socio.
        # Requisito: debe existir un socio con el DNI suministrado.
        for pelicula in self.peliculas:
            if pelicula.titol == titulo and pelicula.alquilada == dni:
                pelicula.alquilada = None
                dias_retraso = pelicula.fecha_alquiler.dias_transcurridos(hoy)
                return
        return -1

    def listado_por_genero(self, genero):
        # Muestra un listado de las peliculas cuyo genero es el indicado.
        # Cada titulo aparece solo una vez. Al lado del titulo aparece
        # una indicacion sobre si hay o no hay ejemplares disponibles
        # para alquilar.
        disponibles = []
        alquiladas = []
        for pelicula in self.peliculas:
            if pelicula.genero == genero:
                if pelicula.alquilada == None and not (pelicula.titulo in disponibles):
                    disponibles.append(pelicula.titulo)
            if pelicula.alquilada != None and not (pelicula.titulo in alquiladas):
                alquiladas.append(pelicula.titulo)
        for titulo in disponibles:
            print(titulo, 'DISPONIBLE')
        for titulo in alquiladas:
            if not (titulo in disponibles):
                print(titulo, 'NO DISPONIBLE')

#.............................................
# Funciones
#.............................................

def menu():
    # Muestra el menu por pantalla y lee una opcion de teclado, que es el
    # resultado devuelto.
    # La funcion se asegura de que la opcion leida este entre 0 y 8.
    print('*** VIDEOCLUB ***')
    print('0) Fijar fecha actual')
    print('1) Dar de alta nuevo socio')
    print('2) Dar de baja nueva pelicula')
    print('3) Dar de alta una nueva pelicula')
    print('4) Dar de baja una pelicula')
    print('5) Alquilar pelicula')
    print('6) Devolver pelicula')
    print('7) Listado por genero')
    print('8) Salir')

    opcion = int(input('Escoge opcion: '))
    while opcion < 0 or opcion > 8:
        opcion = input(input('Escoge opcion (entre 0 y 9): '))
    return opcion

def nuevo_socio():
    # Pide por teclado los datos de un nuevo socio y devuelve un objeto
    # de la clase Socio.
    dni = input('DNI: ')
    nombre = input('Nombre: ')
    telefono = input('Telefono: ')
    domicilio = input('Domicilio: ')
    return Socio(dni, nombre, telefono, domicilio)

def nueva_pelicula():
    # Pide por teclado los datos de una nueva pelicula y devuelve un
    # objeto de la clase Pelicula.
    titulo = input('Titulo: ')
    genero = input('Genero: ')
    dias_permitidos = input('Dias permitidos: ')
    return Pelicula(titulo, genero, dias_permitidos)

#-------------------------------------------------------------
# Programa principal
#-------------------------------------------------------------

# Fijar fecha actual
today = date.today()

videoclub = Videoclub()

opcion = menu()
while opcion != 8:

    if opcion == 0:
        print('Cambiar fecha actual')
        hoy = date.today()
        print('Hoy es:', hoy)

    elif opcion == 1:
        print('Alta de socio')
        socio = nuevo_socio()
        if videoclub.contiene_socio(socio.dni):
            print('Ya existia un socio con DNI', dni)
        else:
            videoclub.alta_socio(socio)

    elif opcion == 2:
            print('Baja de socio')
            dni = input('DNI: ')
            if videoclub.contiene_socio(dni):
                videoclub.baja_socio( dni )
                print('Socio con DNI', dni, 'dado de baja')
            else:
                print('No existe ningun socio con DNI', dni)

    elif opcion == 3:
        print('Alta de pelicula')
        pelicula = nueva_pelicula()
        ejemplares = int(input('Ejemplares: '))
        videoclub.alta_pelicula(pelicula, ejemplares)

    elif opcion == 4:
        print('baja de pelicula')
        titulo = input('Titulo: ')
        ejemplares = int(input('Ejemplares: '))
        bajas = videoclub.baja_pelicula(titulo, ejemplares)
        if bajas < ejemplares:
            print('Solo puede dar de baja', bajas, 'ejemplares')
        else:
            print('Operacion realizada')

    elif opcion == 5:
        print('Alquier pelicula')
        titulo = input('Titulo de la pelicula: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            if videoclub.alquilar_pelicula(titulo, dni):
                print('Operacion realizada')
            else:
                print('La pelicula no está disponible')
        else:
            if not hay_pelicula:
                print('No hay pelicula titulada', titulo)
            if not hay_socio:
                print('No hay socio con DNI', dni)

    elif opcion == 6:
        print('Devolver pelicula')
        titulo = input('Titulo de la pelicula: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            resultado = videoclub.devolver_pelicula(titulo, dni)
            if resultado == 0:
                print('Operacion realizada')
            elif resultado > 0:
                print ('Pelicula entregada con un retraso de', resultado, 'dias')
            else:
                print('La pelicula', titulo, 'no est� alquilada al socio', dni)
        else:
            if not hay_pelicula:
                print('No hay pelicula titulada', titulo)
            if not hay_socio:
                print('No hay socio con DNI', dni)

    elif opcion == 7:
        print('Listado por genero')
        genero = input('Genero: ')
        videoclub.listado_por_genero(genero)

    opcion = menu()