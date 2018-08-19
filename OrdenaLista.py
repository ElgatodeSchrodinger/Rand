#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 02:20:19 2018

@author: leomax
"""

print("---Practica de Ordenamiento---")



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
        result = ""
        add=""
        while(aux != None):
            add = ""
            add = "|" +str(aux.obtenerDato())+ "| "
            aux = aux.obtenerSiguiente()
            if(aux != None):
                add += "──> "
            result += add
        print(result)
        print("--end--")
        
def display(cabeza):
        aux = cabeza
        result = ""
        add=""
        while(aux != None):
            add = ""
            add = "|" +str(aux.obtenerDato())+ "| "
            aux = aux.obtenerSiguiente()
            if(aux != None):
                add += "──> "
            result += add
        print(result)
        print("--END--")


def ordenar(cabeza):
    
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
        
    display(feik.obtenerSiguiente())
    """    
        print("La cabeza es ->",cabeza.obtenerDato())
        print("Menor es -> ",menor.obtenerDato())
        print("Pre es -> ",pre)
        print("aux es -> ",aux)
        print("Flag es -> ", flag)
        
        display(cabeza)
        print("----------ENDBUCLE-------------")
    
    
     INTENTO FALLIDO
    flag = cabeza
    pre = Nodo(None)
    pre.asignarSiguiente(cabeza)
    while(flag.obtenerSiguiente() != None):
        preaux= pre
        flip = pre
        menorb = flag
        while (flip.obtenerSiguiente()!= None):
            if(flip.obtenerSiguiente().obtenerDato() < menorb.obtenerDato()):
                menorb = flip
            flip = flip.obtenerSiguiente()
        while(preaux.obtenerSiguiente() != flag):
            preaux = preaux.obtenerSiguiente()
        menor = menorb.obtenerSiguiente()
        menorb.asignarSiguiente(flag)
        preaux.asignarSiguiente(menor)
        var = menor.obtenerSiguiente()
        menor.asignarSiguiente(flag.obtenerSiguiente())
        flag.asignarSiguiente(var)
        flag = flag.obtenerSiguiente()
        
    cabeza= pre.obtenerSiguiente()
    """
    """
    pre = Nodo(None)
    pre.asignarSiguiente(cabeza)
    while(flag.obtenerSiguiente() != None):
        preaux = pre
        aux = flag.obtenerSiguiente()
        menor = flag
        
        ## Obtener el menor de la lista
        while (aux!= None):
            if(aux.obtenerDato() < menor.obtenerDato()):
                menor = aux
            aux = aux.obtenerSiguiente()
        print("El menor es -> ",menor.obtenerDato())
        
        while(preaux.obtenerSiguiente() != menor):
            preaux = preaux.obtenerSiguiente()
        preaux.asignarSiguiente(menor.obtenerSiguiente())
        menor.asignarSiguiente(pre)
        cabeza = menor
    ## END
    
        """
        
repeticiones = int(input("Ingrese el numero de repeticiones: "))
miLista = Lista(0)
while(repeticiones > 0):
    dato = int(input("Ingrese un numero: "))
    miLista.agregarElemento(dato)
    repeticiones -= 1

print("Antes de Ordenar: ")    
miLista.display()

print("Despues de Ordenar: ")
ordenar(miLista.obtenerPrimero())
    
    
    
    
    