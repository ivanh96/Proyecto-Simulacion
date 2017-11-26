import itertools
import random as rand
import simpy

maxlatas = 200     # latas totales en la maquina
lata1 = 100
intervalo = [30, 300]        # generar una persona entre [min,max] segundos
ttotal = 2000            # tiempo total en segundos

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
        return 0
    if r >= 0.01005025126 and r < 0.3467336683:
        return 1
    if r >= 0.3467336683 and r < 0.8341708543:
        return 2
    if r >= 0.8341708543 and r < 0.9497487437:
        return 3
    if r >= 0.9497487437 and r < 0.9748743719:
        return 4
    if r >= 0.9748743719 and r < 0.9899497487:
        return 5
    if r >= 0.9899497487 and r < 0.9999997487:
        return 6
    if r >= 0.9999997487 and r < 1:
        return 7

# funcion genero
# devuelve un valor entre 0 y 1 para asignar genero siguiendo la distribucion planteada
def genero():
    r = rand.random()
    if r <0.4120603015:
        return 0
    if r >= 0.4120603015 and r < 1:
        return 1
    
def persona(nombre, env, dispensadora, bebida):
    print('%s llega a la dispensadora en %.1f segundos.'  % (nombre, env.now))
    with dispensadora.request() as req:
        start = env.now
        if bebida == 0:
            yield bebida0.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA0 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 1:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA1 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 2:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA2 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 3:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA3 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 4:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA4 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 5:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA5 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 6:
           yield bebida1.get(1)
           yield env.timeout(rand.random()*10)
           print('%s compra una LATA6 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 7:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA7 en %.1f seconds.' % (nombre, env.now - start))
            
        if bebida == 8:
            yield bebida1.get(1)
            yield env.timeout(rand.random()*10)
            print('%s compra una LATA8 en %.1f seconds.' % (nombre, env.now - start))

            
def generar_persona(env, dispensadora, bebida1):
    for i in itertools.count():
        yield env.timeout(rand.randint(*intervalo))
        nombre = 'genero'+repr(genero())+'edad'+repr(edad())
        lata = bebida()
        env.process(persona(nombre, env, dispensadora, lata))


env = simpy.Environment()
dispensadora = simpy.Resource(env, 1)
bebida0 = simpy.Container(env,maxlatas, init= lata1)
bebida1 = simpy.Container(env,maxlatas, init= lata1)
env.process(generar_persona(env, dispensadora, bebida))
env.run(until=ttotal)

