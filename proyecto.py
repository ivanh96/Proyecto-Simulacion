import itertools
import random as rand
import simpy


maxlatas = 200     # latas totales en la maquina
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
    
def persona(nombre, env, dispensadora, bebida1):
    print('%s arriving at gas station at %.1f' % (nombre, env.now))
    with dispensadora.request() as req:
        start = env.now
        # Get the required amount of fuel
        liters_required = 1
        yield bebida1.get(liters_required)

        # The "actual" refueling process takes some time
        yield env.timeout(liters_required)

        print('%s finished refueling in %.1f seconds.' % (nombre, env.now - start))

def generar_persona(env, dispensadora, bebida1):
    for i in itertools.count():
        yield env.timeout(rand.randint(*intervalo))
        nombre = 'genero'+repr(genero())+'edad'+repr(edad())
        env.process(persona(nombre, env, dispensadora, bebida1))


# Setup and start the simulation
print('Gas Station refuelling')

# Create environment and start processes
env = simpy.Environment()
dispensadora = simpy.Resource(env, 1)
bebida1 = simpy.Container(env,maxlatas, init= maxlatas)
env.process(generar_persona(env, dispensadora, bebida1))

# Execute!
env.run(until=ttotal)
