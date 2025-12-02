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




main()