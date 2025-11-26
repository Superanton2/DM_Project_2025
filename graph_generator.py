import random

def graph_generator():
    vertex = input("Enter number of vertexes in range 20 to 200: ") # кількість вершин

    while True:
        while not vertex.isdigit():
            vertex = input("Enter digits only. Enter number of vertexes in range 20 to 200: ")

        if 20 <= int(vertex) <= 200:
            vertex = int(vertex)
            break
        else:
            vertex = input("Enter digits in range 20 to 200 only. Enter number of vertexes in range 20 to 200: ")

    density = input("Enter density in range 0 to 1: ") # очікувана щільність(відношення к-сті утворених графів до к-сті можливих)
    while True:

        try:
            density = float(density)
        except ValueError:
            density = input("Enter numbers only. Enter density in range 0 to 1: ")
            continue

        if 0 <= float(density) <= 1:
            density = float(density)
            break
        else:
            density = input("Enter density in range 0 to 1 only: ")


    # створюємо словник усіх можливих пар, окрім петель. Для кожної пари значення 0(нема графу) або 1(є граф)

    adj_matrix = {}
    for num1 in range(1, vertex+1):
        for num2 in range(num1 + 1, vertex+1):
            if num1 == num2:
                pass
            else:
                key = (num1, num2)
                adj_matrix.setdefault(key)

    # пишемо алгоритм Ердеша-Реньї, який вставлятиме в рандомні місця в матриці одинички(створюватиме графи) основуючись на заданій щільності

    counter = len(adj_matrix)
    print(f"The max possible number of  directed acyclic graph is {counter}")
    while counter != 0:
        for key in adj_matrix:
            chance = random.uniform(0, 1)
            if chance < 1 - density:
                adj_matrix[key] = 0
                counter -= 1
                continue
            else:
                adj_matrix[key] = 1
                counter -= 1
                continue

    graphs = []
    for key in adj_matrix:
        if adj_matrix[key] == 1:
            graphs.append(key)

    print(f"The number of generated graph is {len(graphs)}")

    return graphs

graph_generator()

