"""
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
"""



from queue import LifoQueue as Pila

# Auxiliar
def ordenar_lista_tuplas(tuplas:list[tuple[int,int]]) -> list[tuple[int,int]]:
    for i in range(len(tuplas)):
        ordenado:bool = True
        for j in range(len(tuplas) - i - 1):
            if tuplas[j][0] < tuplas[j+1][0]:
                tuplas[j], tuplas[j+1] = tuplas[j+1], tuplas[j] 
                ordenado = False
        if ordenado: 
            break


def car_fleet(target:int, position:list[int], speed:list[int]) -> int:
    pares_pos_vel:list[tuple[int,int]] = []
    for i in range(len(position)):
        pares_pos_vel.append((position[i], speed[i]))
    
    ordenar_lista_tuplas(pares_pos_vel)
    print(pares_pos_vel)
    
    llegadas:Pila = Pila()
    for posicion, velocidad in pares_pos_vel:
        tiempo:float = (target - posicion) / velocidad
        if llegadas.empty():
            llegadas.put(tiempo)
        else:
            tiempo_anterior:float = llegadas.get()
            llegadas.put(tiempo_anterior)
            if tiempo > tiempo_anterior:
                llegadas.put(tiempo)
    
    contador:int = 0
    while not llegadas.empty():
        contador += 1
        llegadas.get()
    
    return contador


print(car_fleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(car_fleet(target = 100, position = [0,2,4], speed = [4,2,1]))