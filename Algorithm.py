def get_vertex(lst: list):
    vertexes = []
    for a, b in lst:
        vertexes.append(a)
        vertexes.append(b)

    vertexes_dict = {k: False for k in vertexes}
    print(vertexes_dict)

    return vertexes_dict



def visit(dict1: dict, lst: list, vertex = None):
    lst_sorted = []

    if vertex is None:
        for v in dict1.keys():
            if not dict1[v]:
                visit(dict1, lst, v)


    dict1[vertex] = True

    for a, b in lst:
        if a == vertex and not dict1[b]:
            visit(dict1, lst, b)
    if vertex != None:
        lst_sorted.insert(0, vertex)

    return lst_sorted


