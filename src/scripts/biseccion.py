import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
x = sp.Symbol('x')

class Biseccion():
    
    def __init__(self):
        self.__df = pd.DataFrame()
        self.__arrayXi = []
        self.__arrayXu = []
        self.__arrayXr = []
        self.__arrayfXi = []
        self.__arrayfXr = []
        self.__arrayfXifXr = []
        self.__arrayEa = []
        self.__arrayContador = []

                        #*SETTERS
    #Ingreso de la funcion
    def setEcuacion(self, funcion):
        eval(funcion)
        self.__funcion = funcion
    
    #Setter para poder ingresar Xi
    def setXi(self, xi):
        self.__xi = float(xi)

    #Setter para ingresar Xu
    def setXu(self, xu):
        self.__xu = float(xu)

    #Setter para el ingreso de epsilon
    def setEps(self, eps):
        self.__eps = float(eps)

    #Setter para ingresar el rango de la grafica 
    def setRango(self, p1, p2):
        self.__p1=float(p1)
        self.__p2=float(p2)

                        #*GETTERS

    def getResultado(self):
        funcion = lambda x: eval(self.__funcion)
        contador = 0
        while abs(self.__xi - self.__xu) >= self.__eps:
            self.__xr = (self.__xi + self.__xu) / 2
            contador = contador + 1
            self.__arrayContador.append(contador)
            self.__arrayXi.append(self.__xi)
            self.__arrayXu.append(self.__xu)
            self.__arrayXr.append(self.__xr)
            self.__arrayfXi.append(funcion(self.__xi))
            self.__arrayfXr.append(funcion(self.__xr))
            self.__arrayEa.append(abs((self.__xi - self.__xu)))
            self.__arrayfXifXr.append(funcion(self.__xi) * funcion(self.__xr))
            #Si se cumple el signo es negativo y limite superior
            #si se cumple se reemplaza el valor de xu por xr
            if((funcion(self.__xi) * funcion(self.__xr)) < 0):
                self.__xu = self.__xr
            
            # si no cumple se reemplanza el valor de xi por xr
            else:
                self.__xi = self.__xr
        return self.__xr

    def getTabla(self):
        self.__df["I"] = self.__arrayContador
        self.__df["Xi"] = self.__arrayXi
        self.__df["Xu"] = self.__arrayXu
        self.__df["Xr"] = self.__arrayXr
        self.__df["f(Xi)"] = self.__arrayfXi
        self.__df["f(Xr)"] = self.__arrayfXr
        self.__df["(f(Xi) * f(Xr))"] = self.__arrayfXifXr
        self.__df["Ea"] = self.__arrayEa

        return self.__df.set_index("I")

    def getGrafico(self):
        funcion = lambda x: eval(self.__funcion)
        m = np.linspace(self.__p1, self.__p2)
        fig, ax = plt.subplots()
        plt.title("Grafico")
        ax.plot(m, funcion(m), label = "Funcion")
        ax.plot(m, funcion(m)*0, label = "Eje X")
        ax.plot(self.__xr, funcion(self.__xr), 'or', label = "Raiz")
        ax.legend()
        ax.grid()
        return fig



def Post(*args, **kwargs):
    funcion = Element("function")
    xi = Element('setXi')
    xu = Element('setXu')
    eps = Element('setEps')
    setLimiteA = Element('setLimiteA')
    setLimiteB = Element('setLimiteB')
    biseccion = Biseccion()
    biseccion.setEcuacion(funcion.value)
    biseccion.setXi(xi.value)
    biseccion.setXu(xu.value)
    biseccion.setEps(eps.value)
    biseccion.setRango(setLimiteA.value, setLimiteB.value)
    
    pyscript.write("getResultado",'<div>Raiz aproximada: {0} </div>'.format(biseccion.getResultado()))
    
    pyscript.write("getTabla","")
    pyscript.write("getGrafico","")
    pyscript.write("getTabla", biseccion.getTabla())
    pyscript.write("getGrafico", biseccion.getGrafico())
#print("\t\t\t ||  𝓑𝓲𝓼𝓮𝓬𝓬𝓲ó𝓷  ||")