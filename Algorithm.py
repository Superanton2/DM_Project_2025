def visit_node(graph: list[tuple[int, int]], vertex: dict[int, bool], current_node: int, sorted_vertex: list[int]) -> list[int]:
    """
    ця функції перевіряє чи відвідали ми всіх сусідів цієї вершини
        якщо всі сусіди відвідані, то вставляє цей елемент першим в список
        якщо ні, то переходить до сусідів і коли води відмічені додає першим в список

    також ця функція відмічає вершини які вона відвідала

    :param graph: тут має бути граф у вихляді [(1, 7), (1, 12), ... ]
    :param vertex: тут мають бути всі вершини і чи відвідали ми ці вершини {1: False, 7: False, 12: False, ... }
    :param current_node: це вершина в якій ми зараз знаходимось
    :param sorted_vertex: це список в який записується послідовність елементів в правильній послідовності

    :return: повертає список в який записується послідовність елементів в правильній послідовності
    """
    # позначаємо що ми відвідали вершину
    vertex[current_node] = True

    # виписуємо всі елементи в які йде звязов з current_node
    neighbor_of_current_node = [edge for edge in graph if edge[0] == current_node]

    # перевіряємо кожен такий звʼязок
    for edge in neighbor_of_current_node:
        # якщо він не відвіданий, то ми відвідуємо його
        if not vertex[edge[1]]:
            visit_node(graph, vertex, edge[1], sorted_vertex)

    # після того як відвідали всі вершини, вставляємо цей елемент першим в список
    sorted_vertex.insert(0, current_node)

    return sorted_vertex



def topological_sort(graph: list[tuple[int, int]], vertex: dict[int, bool]) -> list[int]:
    """
    це тіло алгоритма топологічного сортування

    :param graph: тут має бути граф у вихляді [(1, 7), (1, 12), ... ]
    :param vertex: тут мають бути всі вершини і чи відвідали ми ці вершини {1: False, 7: False, 12: False, ... }
    :return: повертає список відсортованих вершин.
             Тобто в якій послідовності їх треба відвідати
    """
    sorted_vertex = []

    # проходимось по кожній вершині
    for node in vertex:
        # якщо вона не відвідана, то відвідуємо її
        if not vertex[node]:
            visit_node(graph, vertex, node, sorted_vertex)


    return sorted_vertex