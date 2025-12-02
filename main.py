from Algorithm import topological_sort

from time import perf_counter

from Algorithm import topological_sort
from graph_generator import graph_generator, get_vertex



def tester(vertex: int, density: float) -> float:
    lst_of_graphs, adj_lst = graph_generator(vertex, density)


    vertex = get_vertex(lst_of_graphs)
    # print(vertex)


    # Start the stopwatch / counter
    time_start = perf_counter()

    # функція
    topological_sort(lst_of_graphs, vertex)

    # Stop the stopwatch / counter
    time_stop = perf_counter()

    return time_stop - time_start


# print(tester(20, 1))



def main():

    for vertex in range(20, 200, 10):
        print(vertex)

        for density in range(10, 100, 10):
            density /= 100
            print(density)

            test_time = tester(vertex, density)


            with open("test.csv", "a") as file:
                to_append = f"{vertex}, {density}, {test_time:10f}\n"
                file.write(to_append)
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