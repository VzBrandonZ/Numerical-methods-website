import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
x=sp.Symbol('x')

class NewtonRaphson():
	
	def __init__(self):
		self.__df = pd.DataFrame()
		self.__arrayXi = []
		self.__arrayfxi = []
		self.__arrayfdxi = []
		self.__arrayEa = []
		self.__arrayContador = []
	#Ingreso de la funcion
	def setEcuacion(self, funcion):
		eval(funcion)
		self.__funcion = funcion
	#setter para poder ingresar xi inicial
	def setXi(self, xi):
		self.__xi=float(xi)

	def setEps(self, eps):
		self.__eps = float(eps)
	#Setter para ingresar el rango de la grafica 
	def setRango(self, p1,p2):
		self.__p1=float(p1)
		self.__p2=float(p2)
	#Proceso de newton raphson con retorno de resultado Getter
	def getResultado(self):
		fun = lambda x: eval(self.__funcion)
		d_fun = lambda x: eval(str(sp.diff(self.__funcion)))
		contador = 0
		while True:
			contador = contador + 1
			self.__arrayContador.append(contador)
			self.__arrayXi.append(self.__xi)

			xn=self.__xi-(fun(self.__xi)/d_fun(self.__xi))
			errorA=np.abs(xn-self.__xi)

			self.__arrayfxi.append(fun(self.__xi))
			self.__arrayfdxi.append(d_fun(self.__xi))
			self.__arrayEa.append(errorA)
			self.__xi = xn
			if self.__eps >= errorA:
				contador = contador + 1
				self.__arrayContador.append(contador)
				self.__arrayfxi.append(fun(self.__xi))
				self.__arrayfdxi.append(d_fun(self.__xi))
				self.__arrayEa.append(errorA)
				self.__arrayXi.append(self.__xi)
				return self.__xi
				

	def getTabla(self):
		self.__df['I'] = self.__arrayContador
		self.__df['Xi'] = self.__arrayXi
		self.__df['f(xi)'] = self.__arrayfxi
		self.__df["f'(xi)"] = self.__arrayfdxi
		self.__df['ErrorAbsoluto'] = self.__arrayEa

		return self.__df.set_index("I")

	#getter para visualizar la grafica
	def getGrafico(self):
		fun= lambda x: eval(self.__funcion)
		m=np.linspace(self.__p1, self.__p2)
		fig, ax = plt.subplots()
		plt.title("Grafico")
		ax.plot(m,fun(m),label="Funcion")
		ax.plot(m,fun(m)*0, label = "Eje X")
		ax.plot(self.__xi,fun(self.__xi), 'or', label='Raíz')
		ax.legend()
		ax.grid()
		return fig






def Post(*args, **kwargs):
	funcion = Element("function")
	xi = Element('setXi')
	eps = Element('setEps')
	setLimiteA = Element('setLimiteA')
	setLimiteB = Element('setLimiteB')
	#print("\t \t||  𝓝𝓮𝔀𝓽𝓸𝓷 𝓡𝓪𝓹𝓱𝓼𝓸𝓷 ||")
	newton = NewtonRaphson()
	newton.setEcuacion(funcion.value)
	newton.setXi(xi.value)
	newton.setEps(eps.value)
	newton.setRango(setLimiteA.value, setLimiteB.value)

	pyscript.write("getResultado",'<div>Raiz aproximada: {0} </div>'.format(newton.getResultado()))
	
	pyscript.write("getTabla","")
	pyscript.write("getGrafico","")
	pyscript.write("getTabla", newton.getTabla())
	pyscript.write("getGrafico", newton.getGrafico())