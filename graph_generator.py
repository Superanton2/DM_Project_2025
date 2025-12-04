import random


def graph_generator(vertex: int, density: float, test = None):
    """
    генератор графів
    герерує список суміжностей та матрицю суміжності
    при тестуванні (test == True) ми не виводимо інформацію про кількість графів задля візуальної чистоти терміналу 

    :param vertex: кількість вершин. Від 20 до 200
    :param density: відсоток того як багато буде зʼєднано. Від 0 до 1
    :return: список суміжності та матрицю суміжності
    """

    # створюємо словник усіх можливих пар, окрім петель (блок який перевіряє чи рівні числа) та циклів. Для кожної пари значення 0(нема графу) або 1(є граф)

    adjacency_matrix = {}
    for num1 in range(1, vertex+1):
        for num2 in range(num1 + 1, vertex+1):
            if num1 == num2:
                pass
            else:
                key = (num1, num2)
                adjacency_matrix.setdefault(key)

    # пишемо алгоритм Ердеша-Реньї, який вставлятиме в рандомні місця в матриці одинички(створюватиме графи) основуючись на заданій щільності

    if test == None or test == False: # при тестуванні (test == True) ми не виводимо інформацію про кількість ребер задля візуальної чистоти терміналу 
        print(f"The max possible number of  directed acyclic graph is {len(adjacency_matrix)}")
    
    for key in adjacency_matrix:
        chance = random.uniform(0, 1)
        if chance < 1 - density:
            adjacency_matrix[key] = 0
        else:
            adjacency_matrix[key] = 1

    graphs = []
    for key in adjacency_matrix:
        if adjacency_matrix[key] == 1:
            graphs.append(key)

    if test == None or test == False: # при тестуванні (test == True) ми не виводимо інформацію про кількість ребер задля візуальної чистоти терміналу 
        print(f"The number of generated graph is {len(graphs)}")

    # пишемо "перекладач" з матриці суміжності у списки суміжності

    adjacency_lst = {}  # список суміжності
    for key in adjacency_matrix:
        if not key in adjacency_lst: # для кожної вершини,  якщо її немає в нашому списку суміжності, то ми створюємо пустий список, в який згодом додаватимемо вершини, до яких від першої йдуть ребра
            adjacency_lst.setdefault(key[0], []).append(key[1])
        else:
            adjacency_lst[key[0]].append(key[1]) # до списку суміжності для кожної вершини ми додаємо вершину, до якої є ребро

    return graphs, adjacency_lst

def get_vertex(graph: list[tuple[int, int]]) -> dict[int, bool]:
    """
    це функція яка з отриманого графа виписує всі вершини які там є і чи відвідали ми цю вершину

    :param graph: отримує грав заданий матрицею суміжності (списком пар)
    :return: повертає словних з вершини і значення чи відвідав ми цю вершину
    """
    vertexes = []
    for first, second in graph:
        vertexes.append(first)
        vertexes.append(second)

    vertexes_dict = {k: False for k in vertexes}


    return vertexes_dict

