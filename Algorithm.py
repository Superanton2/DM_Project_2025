def visit_vertex_matrix(graph: list[tuple[int, int]], vertex: dict[int, bool], current_vertex: int, sorted_vertex: list[int]) -> list[int]:
    """
    ця функції перевіряє чи відвідали ми всіх сусідів цієї вершини
        якщо всі сусіди відвідані, то вставляє цей елемент першим в список
        якщо ні, то переходить до сусідів і коли води відмічені додає першим в список

    також ця функція відмічає вершини які вона відвідала

    :param graph: тут має бути граф у вигляді [(1, 7), (1, 12), ... ]
    :param vertex: тут мають бути всі вершини і чи відвідали ми ці вершини {1: False, 7: False, 12: False, ... }
    :param current_vertex: це вершина в якій ми зараз знаходимось
    :param sorted_vertex: це список в який записується послідовність елементів в правильній послідовності

    :return: повертає список в який записується послідовність елементів в правильній послідовності
    """
    # позначаємо що ми відвідали вершину
    vertex[current_vertex] = True

    # виписуємо всі елементи в які йде звязов з current_vertex
    neighbor_of_current_vertex = [edge for edge in graph if edge[0] == current_vertex]

    # перевіряємо кожен такий звʼязок
    for edge in neighbor_of_current_vertex:
        # якщо він не відвіданий, то ми відвідуємо його
        if not vertex[edge[1]]:
            visit_vertex_matrix(graph, vertex, edge[1], sorted_vertex)

    # після того як відвідали всі вершини, вставляємо цей елемент першим в список
    sorted_vertex.insert(0, current_vertex)

    return sorted_vertex



def topological_sort_matrix(graph: list[tuple[int, int]], vertexes: dict[int, bool]) -> list[int]:
    """
    це тіло алгоритма топологічного сортування

    :param graph: тут має бути граф у вигляді [(1, 7), (1, 12), ... ]
    :param vertex: тут мають бути всі вершини і чи відвідали ми ці вершини {1: False, 7: False, 12: False, ... }
    :return: повертає список відсортованих вершин.
             Тобто в якій послідовності їх треба відвідати
    """
    sorted_vertexes = []

    # проходимось по кожній вершині
    for vertex in vertexes:
        # якщо вона не відвідана, то відвідуємо її
        if not vertexes[vertex]:
            visit_vertex_matrix(graph, vertexes, vertex, sorted_vertexes)


    return sorted_vertexes



def visit_vertex_list(graph: dict[int, list[int]], vertexes: dict[int, bool], current_vertex: int, sorted_vertex: list[int]) -> list[int]:
    # позначаємо що ми відвідали вершину
    vertexes[current_vertex] = True

    # перевіряємо кожен такий звʼязок
    for vertex1, vertexes2 in graph.items():
        # якщо він не відвіданий, то ми відвідуємо його
        for vertex2 in vertexes2:
            if vertex1 == current_vertex:
                if not vertexes[vertex2]:
                    visit_vertex_list(graph, vertexes, vertex2, sorted_vertex)

    # після того як відвідали всі вершини, вставляємо цей елемент першим в список
    sorted_vertex.insert(0, current_vertex)

    return sorted_vertex



def topological_sort_list(graph: dict[int, list[int]], vertexes: dict[int, bool]) -> list[int]:
    sorted_vertexes = []

    # проходимось по кожній вершині
    for vertex in vertexes:
        # якщо вона не відвідана, то відвідуємо її
        if not vertexes[vertex]:
            visit_vertex_list(graph, vertexes, vertex, sorted_vertexes)

    return sorted_vertexes