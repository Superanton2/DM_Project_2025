import time
import sys

from Algorithm import topological_sort_matrix, topological_sort_list
from graph_generator import graph_generator, get_vertex
from helper_function import lst_input_to_int, input_to_int, RED, RESET
from data_visualization import  plot_test_on_vertex, plot_test_on_density


def time_tracker(vertex: int, density: float, matrix= True) -> float:
    lst_of_graphs, adj_lst = graph_generator(vertex, density, test=True)

    vertex = get_vertex(lst_of_graphs)
    if matrix:

        # Start the stopwatch / counter
        time_start = time.perf_counter()

        # функція
        topological_sort_matrix(lst_of_graphs, vertex)

        # Stop the stopwatch / counter
        time_stop = time.perf_counter()

    else:

        # Start the stopwatch / counter
        time_start = time.perf_counter()

        # функція
        topological_sort_list(adj_lst, vertex)

        # Stop the stopwatch / counter
        time_stop = time.perf_counter()

    return time_stop - time_start



def test_on_vertex():
    print()
    test_type = lst_input_to_int(["matrix", "list"])
    vertex = input_to_int("On what number of vertices will we make the test(20 to 200): ", min_value= 20, max_value= 200)

    filename = f'tests_vertex/test_{vertex}.csv'


    for density in range(10, 100, 10):
        density /= 100

        for _ in range(20):

            if test_type == 1:
                test_time = time_tracker(vertex, density, matrix=True)
            else:
                test_time = time_tracker(vertex, density, matrix=False)


            with open(f"{filename}", "a") as file:
                to_append = f"{vertex}, {density}, {test_time:10f}\n"
                file.write(to_append)

    print("Test finished", end= " ")
    if test_type == 1:
        print("for matrix")
    else:
        print("for list")

    print(f"Now yon can see your results in directory {filename}")

    print(f"Generating plot")
    print(f"{RED}ТО MOVE FURTHER FIRST CLOSE PLOT WINDOW{RESET}")
    plot_test_on_vertex(vertex, filename)


def test_on_density():
    print()
    test_type = lst_input_to_int(["matrix", "list"])
    density = input_to_int("On what persent of density will we make the test(0 to 100): ", min_value=0, max_value=100)

    filename = f'tests_density/test_{density}.csv'

    for vertex in range(20, 201, 10):

        for _ in range(20):
            if test_type == 1:
                test_time = time_tracker(vertex, density, matrix=True)
            else:
                test_time = time_tracker(vertex, density, matrix=False)

            with open(f"{filename}", "a") as file:
                to_append = f"{vertex}, {density}, {test_time:10f}\n"
                file.write(to_append)

    print("Test finished")
    print(f"Now yon can see your results in directory {filename}")

    print(f"Generating plot")
    print(f"{RED}ТО MOVE FURTHER FIRST CLOSE PLOT WINDOW{RESET}")
    plot_test_on_density(density, filename)


    print()




def test_parameters():

    while True:
        choice = lst_input_to_int(["Test on number of vertex", "Test on density", "Quit   ₍^. .^₎⟆"])
        if choice == 1:
            test_on_vertex()
        else:
            test_on_density()

        print()
        choice = lst_input_to_int(["Continue", "Quit"])
        if choice == 1:
            continue
        else:
            break

    return


def test_all():

    print("Start testing for matrix")

    for vertex in range(20, 201, 10):
        with open(f"tests_all/matrix/test_{vertex}.csv", "w") as file:
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
                test_time = time_tracker(vertex, density,  matrix=True)

                with open(f"tests_all/matrix/test_{vertex}.csv", "a") as file:
                    to_append = f"{vertex}, {density}, {test_time:10f}\n"
                    file.write(to_append)
    print("\nFinish testing")


    print("Start testing for list")

    for vertex in range(20, 201, 10):
        with open(f"tests_all/list/test_{vertex}.csv", "w") as file:
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
                test_time = time_tracker(vertex, density, matrix=False)

                with open(f"tests_all/list/test_{vertex}.csv", "a") as file:
                    to_append = f"{vertex}, {density}, {test_time:10f}\n"
                    file.write(to_append)
    print("\nFinish testing")

    print("Now yon can see your results in directory tests_all/")
    print("There are 2 directory. One for matrix and one for list")