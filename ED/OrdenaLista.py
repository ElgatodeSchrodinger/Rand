#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 02:20:19 2018

@author: leomax
"""

print("\t\t\t--- Ejercicio de Ordenamiento ---")
print("\t\t\t      --- Selection Sort ---")


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
    def asignarPrimero(self,dato):
        self.cabeza = dato
def longitud(cabeza):
        contador = 0
        aux = cabeza
        while(aux!=None):
            contador += 1
            aux = aux.obtenerSiguiente()
        return contador
        
def display(cabeza):
        aux = cabeza
        result = "\t\t\t"
        add=""
        while(aux != None):
            add = ""
            add = "|" +str(aux.obtenerDato())+ "| "
            aux = aux.obtenerSiguiente()
            if(aux != None):
                add += "──> "
            result += add
        print(result)


def ordenar(lista):
    
    cabeza = lista.obtenerPrimero()
    feik = Nodo(None)
    feik.asignarSiguiente(cabeza)
    flag = cabeza
    while(flag != None):
        pre = feik
        menor = flag
        aux = flag
        ## Obtener el menor de la lista
        while (aux!= None):
            if(aux.obtenerDato() < menor.obtenerDato()):
                menor = aux
            aux = aux.obtenerSiguiente()
            ## print("Menor es -> ",menor.obtenerDato())
        ## print("-----------------------")
        while(pre.obtenerSiguiente() != menor ):
            pre = pre.obtenerSiguiente()
            
        if(menor == flag):
            flag = flag.obtenerSiguiente()
        pre.asignarSiguiente(menor.obtenerSiguiente())
        menor.asignarSiguiente(feik.obtenerSiguiente())
        feik.asignarSiguiente(menor)
    cabeza = feik.obtenerSiguiente()  
    lista.asignarPrimero(cabeza)
    display(cabeza)
   
    
    
repeticiones = int(input("\tIngrese el numero de repeticiones: "))
miLista = None
while(repeticiones > 0):
    dato = int(input("\t\tIngrese un numero: "))
    if(miLista):
        miLista.agregarElemento(dato)
    else:
        miLista = Lista(dato)
    repeticiones -= 1
print("\t───────────────────────────────────────────")
print("\t\tAntes de Ordenar: ")    
display(miLista.obtenerPrimero())

print("\t\tDespues de Ordenar: ")
ordenar(miLista)

# ENDLINE
endline = ""
cant= (longitud(miLista.obtenerPrimero())*7-3)//2
for i in range(cant):
    endline+="-"
endline+="END"
for i in range(cant):
    endline+="-"
print("\t\t\t",endline)
    
    