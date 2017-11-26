import itertools
import random as rand
import simpy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

print("Bienvenido al simulador de máquina dispensadora de bebidas UVG 2017")
print("")
print("La máquina dispensa 9 distintos tipos de bebidas. A continuación, se te pedira que ingreses la cantidad de latas inicial para cada una de ellas.")
print("Debes tomar en cuenta que la máquina únicamente puede almacenar hasta 100 latas de cada tipo.")
print("")
enter = input("Presiona enter para continuar.")
maxlatas = 100     # latas totales en la maquina
inicial=[0 for i in range(9)] #valores iniciales que se le metieron a la maquina
vendidos=[0 for i in range(9)]    #conteo de cuantas bebidas se han vendido
edades=[0 for i in range(8)]
lata0 = 101
while(lata0>maxlatas):
    lata0=int(input("Ingresa la cantidad de latas de Coca Cola iniiciales (no puede ser mayor a 100):"))
inicial[0]=lata0
lata1 = 101
while(lata1>maxlatas):
    lata1=int(input("Ingresa la cantidad de latas de Jugo de Naranja iniiciales (no puede ser mayor a 100):"))
inicial[1]=lata1
lata2 = 101
while(lata2>maxlatas):
    lata2=int(input("Ingresa la cantidad de latas de Naranjada con Soda iniiciales (no puede ser mayor a 100):"))
inicial[2]=lata2
lata3 = 101
while(lata3>maxlatas):
    lata3=int(input("Ingresa la cantidad de latas de Limonada con Soda iniiciales (no puede ser mayor a 100):"))
inicial[3]=lata3
lata4 = 101
while(lata4>maxlatas):
    lata4=int(input("Ingresa la cantidad de latas de Agua Pura iniiciales (no puede ser mayor a 100):"))
inicial[4]=lata4
lata5 = 101
while(lata5>maxlatas):
    lata5=int(input("Ingresa la cantidad de latas de Orange Crush iniiciales (no puede ser mayor a 100):"))
inicial[5]=lata5
lata6 = 101
while(lata6>maxlatas):
    lata6=int(input("Ingresa la cantidad de latas de Jugo Kern's iniiciales (no puede ser mayor a 100):"))
inicial[6]=lata6
lata7 = 101
while(lata7>maxlatas):
    lata7=int(input("Ingresa la cantidad de latas de gaseosa de Uva iniiciales (no puede ser mayor a 100):"))
inicial[7]=lata7
lata8 = 101
while(lata8>maxlatas):
    lata8=int(input("Ingresa la cantidad de latas de Coca Cola Light iniiciales (no puede ser mayor a 100):"))
inicial[8]=lata8
intervalo = [30, 600]        # generar una persona entre [min,max] segundos

print("")
ttotal = int(input("Ahora ingresa el tiempo que deseas que tarde la simulación, en segundos:"))            # tiempo total en segundos
enter=input("Perfecto, todos los datos listos. Presiona 'Enter' para empezar la simulación.")
# funcion bebida
# devuelve un valor entre 0 y 8 para asignar bebida siguiendo la distribucion planteada
def bebida():
    r = rand.random()
    if r <0.3266331658:
        return 0
    if r >= 0.3266331658 and r < 0.4070351759:
        return 1
    if r >= 0.4070351759 and r < 0.4974874372:
        return 2
    if r >= 0.4974874372 and r < 0.5979899497:
        return 3
    if r >= 0.5979899497 and r < 0.6984924623:
        return 4
    if r >= 0.6984924623 and r < 0.7788944724:
        return 5
    if r >= 0.7788944724 and r < 0.8190954774:
        return 6
    if r >= 0.8190954774 and r < 0.8693467337:
        return 7
    if r >= 0.8693467337 and r < 1:
        return 8

# funcion edad
# devuelve un valor entre 0 y 7 para asignar edad siguiendo la distribucion planteada
def edad():
    r = rand.random()
    if r <0.01005025126:
        edades[0]+=1
        return "entre 1 y 10 años"
    if r >= 0.01005025126 and r < 0.3467336683:
        edades[1]+=1
        return "entre 11 y 20 años"
    if r >= 0.3467336683 and r < 0.8341708543:
        edades[2]+=1
        return "entre 21 y 30 años"
    if r >= 0.8341708543 and r < 0.9497487437:
        return "entre 31 y 40 años"
        edades[3]+=1
    if r >= 0.9497487437 and r < 0.9748743719:
        edades[4]+=1
        return "entre 41 y 50 años"
    if r >= 0.9748743719 and r < 0.9899497487:
        edades[5]+=1
        return "entre 51 y 60 años"
    if r >= 0.9899497487 and r < 0.9999997487:
        edades[6]+=1
        return "entre 61 y 70 años"
    if r >= 0.9999997487 and r < 1:
        edades[7]+=1
        return "entre 71 y 80 años"

# funcion genero
# devuelve un valor entre 0 y 1 para asignar genero siguiendo la distribucion planteada
def genero():
    r = rand.random()
    if r <0.4120603015:
        return "Mujer"
    if r >= 0.4120603015 and r < 1:
        return "Hombre"
    
def persona(nombre, env, dispensadora, bebida):
    print('%s llega a la dispensadora en el segundo %.1f.'  % (nombre, env.now))
    with dispensadora.request() as req:
        start = env.now
        if bebida == 0:
            vendidos[0]+=1
            yield bebida0.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Coca Cola en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 1:
            vendidos[1]+=1
            yield bebida1.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra un Jugo de Naranja en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 2:
            vendidos[2]+=1
            yield bebida2.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Naranjada con Soda en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 3:
            vendidos[3]+=1
            yield bebida3.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Limonada con Soda en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 4:
            vendidos[4]+=1
            yield bebida4.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra un Agua Pura en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 5:
            vendidos[5]+=1
            yield bebida5.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Orange Crush en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 6:
           vendidos[6]+=1
           yield bebida6.get(1)
           yield env.timeout(rand.randint(10,30))
           print('%s compra un Jugo Kerns en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 7:
            vendidos[7]+=1
            yield bebida7.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Gaseosa de Uva en %.1f segundos.' % (nombre, env.now - start))
            
        if bebida == 8:
            vendidos[8]+=1
            yield bebida8.get(1)
            yield env.timeout(rand.randint(10,30))
            print('%s compra una Coca Cola Light en %.1f segundos.' % (nombre, env.now - start))

            
def generar_persona(env, dispensadora, bebida1):
    for i in itertools.count():
        yield env.timeout(rand.randint(*intervalo))
        nombre = 'Una persona de genero '+repr(genero())+' con edad '+repr(edad())
        env.process(persona(nombre, env, dispensadora, bebida()))


env = simpy.Environment()
dispensadora = simpy.Resource(env, 1)

bebida0 = simpy.Container(env,maxlatas, init= lata0)
bebida1 = simpy.Container(env,maxlatas, init= lata1)
bebida2 = simpy.Container(env,maxlatas, init= lata2)
bebida3 = simpy.Container(env,maxlatas, init= lata3)
bebida4 = simpy.Container(env,maxlatas, init= lata4)
bebida5 = simpy.Container(env,maxlatas, init= lata5)
bebida6 = simpy.Container(env,maxlatas, init= lata6)
bebida7 = simpy.Container(env,maxlatas, init= lata7)
bebida8 = simpy.Container(env,maxlatas, init= lata8)

env.process(generar_persona(env, dispensadora, bebida))
env.run(until=ttotal)

print("")
enter=input("Presiona enter para ver un gráfico representando las edades de los clientes.")
x=["entre 1 y 10", "entre 11 y 20","entre 21 y 30","entre 31 y 40", "entre 41 y 50","entre 51 y 60","entre 61 y 70", "entre 71-80" ]
y_pos = np.arange(len(edades))
plt.bar(y_pos,edades,align='center',alpha=0.5)
plt.xticks(y_pos,x)
plt.ylabel('Cantidad de clientes')
plt.xlabel('Rango de edad')
plt.title('Frecuencia de la edad')
plt.show()
print("")
enter=input("Presiona enter para ver un gráfico representando las bebidas que se compraron")
x=["Coca Cola", "Jugo de Naranja","Naranjada con Soda","Limoonada con Soda", "Agua Pura","Orange Crush","Jugo Kerns", "Uva","Coca Cola Light" ]
y_pos = np.arange(len(vendidos))
plt.bar(y_pos,vendidos,align='center',alpha=0.5)
plt.xticks(y_pos,x)
plt.ylabel('Cantidad de bebidas')
plt.xlabel('Bebida')
plt.title('Frecuencia de las bebidas vendidas')
plt.show()
