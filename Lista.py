#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:54:22 2018

@author: leomax
"""

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
        
class Lista:
    def __init__(self,datoInicial):
        self.ultimo = Nodo(datoInicial)
        self.cabeza = self.ultimo
    def agregarElemento(self,entrada):
        nuevo = Nodo(entrada)
        self.ultimo.asignarSiguiente(nuevo)
        self.ultimo = nuevo
    def obtenerUltimo(self):
        return self.ultimo
    def obtenerPrimero(self):
        return self.cabeza
    def longitud(self):
        contador = 0
        aux = self.cabeza
        while(aux!=None):
            contador += 1
            aux = aux.obtenerSiguiente()
        return contador
    def display(self):
        aux = self.cabeza
        while(aux != None):
            print(aux.obtenerDato())
            aux = aux.obtenerSiguiente()
            print("....")
        print("--end--")
        
        
miLista = Lista(12)
miLista.agregarElemento(13)
miLista.agregarElemento(14)
miLista.agregarElemento(15)
miLista.agregarElemento(16)

print("La longitud de mi lista es -> ",miLista.longitud())
print("Mi lista es : ")
print(miLista.display())
"""
cabeza= Nodo(10)
siguiente = Nodo(9)

cabeza.asignarSiguiente(siguiente)
contador = 4
while(contador > 0):
    dato = input("Ingrese un numero: ")
    nuevo = Nodo(dato)
    siguiente.asignarSiguiente(nuevo)
    siguiente = nuevo
    contador -= 1

aux= cabeza
while(aux!=None):
    print(aux.obtenerDato())
    aux=aux.obtenerSiguiente()
    
    
"""
