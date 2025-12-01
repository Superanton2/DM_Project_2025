from Algorithm import visit, get_vertex

from time import perf_counter
from graph_generator import graph_generator


def tester(vertex: int, density: float) -> float:
    lst_of_graphs = graph_generator()
    vertex = get_vertex(lst_of_graphs)


    # Start the stopwatch / counter
    time_start = perf_counter()

    # функція
    print(visit(vertex, lst_of_graphs))

    # Stop the stopwatch / counter
    time_stop = perf_counter()

    return time_stop - time_start


def main():

    for vertex in range(20, 200, 10):
        print(vertex)

        for density in range(10, 100, 10):
            density /= 100
            print(density)



        # with open("test.csv", "a") as file:
        #     pass
        # pass
        #
# не менше п’яти різних значень щільності та не менше
# десяти різних розмірів графу



main()

    # vertex = input("Enter number of vertexes in range 20 to 200: ")  # кількість вершин
#     while True:
#         while not vertex.isdigit():
#             vertex = input("Enter digits only. Enter number of vertexes in range 20 to 200: ")
#
#         if 20 <= int(vertex) <= 200:
#             vertex = int(vertex)
#             break
#         else:
#             vertex = input("Enter digits in range 20 to 200 only. Enter number of vertexes in range 20 to 200: ")
#
#     density = input("Enter density in range 0 to 1: ") # очікувана щільність(відношення к-сті утворених графів до к-сті можливих)
#     while True:
#
#         try:
#             density = float(density)
#         except ValueError:
#             density = input("Enter numbers only. Enter density in range 0 to 1: ")
#             continue
#
#         if 0 <= float(density) <= 1:
#             density = float(density)
#             break
#         else:
#             density = input("Enter density in range 0 to 1 only: ")


# 0.0001031670
# 0.00009045800000029303