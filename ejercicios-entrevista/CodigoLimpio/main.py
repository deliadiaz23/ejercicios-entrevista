import random

def get_random_pivot(lista):
    return random.choice(lista)

def get_menores(lista, pivot):
    return [x for x in lista if x < pivot]

def get_mayores(lista, pivot):
    return [x for x in lista if x > pivot]

def get_iguales(lista, pivot):
    return [x for x in lista if x == pivot]

def ordenar_lista(lista):
    if not all([isinstance(x, int) for x in lista]):
        return "Todos los elementos deben ser enteros"
    if len(lista) < 2:
        return lista
    pivot = get_random_pivot(lista)
    return ordenar_lista(get_menores(lista, pivot)) + get_iguales(lista, pivot) + ordenar_lista(get_mayores(lista, pivot))

if __name__ == '__main__':
    print(ordenar_lista([6,52,7,58,2,40,69,85,0,48,41,45,87,963,55,48]))
