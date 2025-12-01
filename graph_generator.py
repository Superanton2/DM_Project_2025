import random


def graph_generator(vertex: int, density: float):

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

    for key in adj_matrix:
        chance = random.uniform(0, 1)
        if chance < 1 - density:
            adj_matrix[key] = 0
        else:
            adj_matrix[key] = 1

    graphs = []
    for key in adj_matrix:
        if adj_matrix[key] == 1:
            graphs.append(key)

    print(f"The number of generated graph is {len(graphs)}")

    # пишемо "перекладач" з матриці суміжності у списки суміжності

    adj_lst = {}  # список суміжності
    for key in adj_matrix:
        if not key in adj_lst:
            adj_lst.setdefault(key[0], []).append(key[1])
        else:
            adj_lst[key[0]].append(key[1])

    return graphs, adj_lst