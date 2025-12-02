import time
import sys

from Algorithm import topological_sort
from graph_generator import graph_generator, get_vertex



def tester(vertex: int, density: float) -> float:
    lst_of_graphs, adj_lst = graph_generator(vertex, density)


    vertex = get_vertex(lst_of_graphs)
    # print(vertex)


    # Start the stopwatch / counter
    time_start = time.perf_counter()

    # функція
    topological_sort(lst_of_graphs, vertex)

    # Stop the stopwatch / counter
    time_stop = time.perf_counter()

    return time_stop - time_start


# print(tester(20, 1))



def main():

    print("Start testing")
    for vertex in range(20, 201, 10):

        with open(f"tests/test_{vertex}.csv", "w") as file:
            file.write("number of vertex,percentage of density,time\n")


        # Форматуємо рядок для відображення прогресу
        output = f"progress: {vertex // 2}%"

        # Виводимо рядок, використовуючи \r для повернення курсора
        sys.stdout.write('\r' + output)

        # Обов'язково викликаємо flush() для негайного відображення в терміналі
        sys.stdout.flush()


        for density in range(10, 100, 10):
            density /= 100


            for _ in range(20):

                test_time = tester(vertex, density)


                with open(f"tests/test_{vertex}.csv", "a") as file:
                    to_append = f"{vertex}, {density}, {test_time:10f}\n"
                    file.write(to_append)
    print("\nFinish testing")


if __name__ == '__main__':
    main()