import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class AproximacionSucesiva():
    def __init__(self):
        # ? dataFrame
        self.__df = pd.DataFrame()
        # ? Arrays para hacer la tabla.
        self.__arrayContador = []
        self.__arrayXi = []
        self.__arrayXiDx = []
        self.__arrayfxi = []
        self.__arrayfxiDx = []
        self.__arrayEa = []
        self.__arrayDeltaX = []

                                #* SETTERS
    #funcion para el ingreso de la ecuacion. (set)
    def setEcuacion(self, funcion):
        eval(funcion)
        self.__funcion = funcion
    
    #Setter para el ingreso del valor en Xi
    def setXi(self, xi):
        self.__xi = float(xi)
    
    #Setter para poder ingresar el valor de epsilon.
    def setEps(self, eps):
        self.__eps = float(eps)

    
    #Setter para poder ingresar el valor de DeltaX.
    def setDeltaX(self, deltaX):
        self.__dx = float(deltaX)

    #Setter para ingresar el rango de la grafica    
    def setRango(self, p1,p2):
        self.__p1=float(p1)
        self.__p2=float(p2)
    
        

                                #* GETTERS
    #Proceso de Aproximaciones sucesivas con retorno de resultado (Getters).
    def getResultado(self):
        f = lambda x: eval(self.__funcion)
        contador = 0
        while True:
            contador = contador + 1
            self.__arrayContador.append(contador)
            self.__arrayXi.append(self.__xi)
            self.__arrayXiDx.append(self.__xi + self.__dx)
            self.__arrayfxi.append(f(self.__xi))
            self.__arrayfxiDx.append(f(self.__xi + self.__dx))
            self.__arrayEa.append(abs(self.__xi - (self.__xi + self.__dx)))
            self.__arrayDeltaX.append(self.__dx)

            if((f(self.__xi) > 0 and f(self.__xi + self.__dx) < 0) or (f(self.__xi) < 0 and f(self.__xi + self.__dx) > 0)):
                self.__dx = self.__dx / 10
            
            if(abs(self.__xi - (self.__xi + self.__dx)) <= self.__eps):
                break
            self.__xi = self.__xi + self.__dx
        return self.__xi
        
        
    def getTabla(self):
        self.__df['I'] = self.__arrayContador
        self.__df['Xi'] = self.__arrayXi
        self.__df['(Xi + ▲x)'] = self.__arrayXiDx
        self.__df['ƒ(Xi)'] = self.__arrayfxi
        self.__df['ƒ(Xi + ▲x)'] = self.__arrayfxiDx
        self.__df['Ea'] = self.__arrayEa
        self.__df['▲x'] = self.__arrayDeltaX
        
        
        return self.__df.set_index("I")

    def getGrafica(self):
        f = lambda x: eval(self.__funcion)
        m = np.linspace(self.__p1, self.__p2)
        fig, ax = plt.subplots()
        plt.title("Grafico")
        ax.plot(m, f(m), label = "Función")
        ax.plot(m, f(m)*0, label = "Eje X")
        ax.plot(self.__xi, f(self.__xi), 'or', label = "Raiz")
        ax.legend()
        ax.grid()
        return fig
    
def Post(*args, **kwargs):
    #tomando los datos del form

    funcion = Element("function")
    xi = Element('setXi')
    deltaX = Element('setDeltaX')
    eps = Element('setEps')
    setLimiteA = Element('setLimiteA')
    setLimiteB = Element('setLimiteB')
    aproxSucesiva = AproximacionSucesiva()
    aproxSucesiva.setEcuacion(funcion.value)
    aproxSucesiva.setXi(xi.value)
    aproxSucesiva.setDeltaX(deltaX.value)
    aproxSucesiva.setEps(eps.value)
    aproxSucesiva.setRango(setLimiteA.value, setLimiteB.value)
    pyscript.write("getResultado",'<div>Raiz aproximada: {0} </div>'.format(aproxSucesiva.getResultado()))

    pyscript.write("getTabla","")
    pyscript.write("getGrafico","")
    pyscript.write("getTabla", aproxSucesiva.getTabla())
    pyscript.write("getGrafico", aproxSucesiva.getGrafica())


#aproxSucesiva.setEcuacion('2.718281828**x - 3*x')
#aproxSucesiva.setXi(0.6)
#aproxSucesiva.setDeltaX(0.1)
#aproxSucesiva.setEps(0.0001)
#aproxSucesiva.setRango(-1, 3)
#aproxSucesiva.getResultado()
#aproxSucesiva.getTabla()




