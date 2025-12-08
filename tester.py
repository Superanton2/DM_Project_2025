import time
import sys
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from Algorithm import topological_sort_matrix
from graph_generator import graph_generator, get_vertex
from helper_function import lst_input_to_int, input_to_int, RED, RESET


def print_single_test(lst_of_graphs: list[tuple[int, int]], vertex: dict[int, bool]):
    """
    намалювати граф по вершинам та ребрам

    :param lst_of_graphs:
    :param vertex:
    :return:
    """
    graph = nx.Graph()


    graph.add_nodes_from(vertex)
    graph.add_edges_from(lst_of_graphs)

    nx.draw(graph, with_labels=True, arrows=True, node_color='lightblue', edge_color='gray', node_size=250)
    plt.axis('off')
    plt.show()

def time_tracker(vertex: int, density: float) -> float:
    lst_of_graphs, adj_lst = graph_generator(vertex, density, test=True)

    vertex = get_vertex(lst_of_graphs)
    # print(vertex)

    # Start the stopwatch / counter
    time_start = time.perf_counter()

    # функція
    topological_sort_matrix(lst_of_graphs, vertex)

    # Stop the stopwatch / counter
    time_stop = time.perf_counter()

    return time_stop - time_start


def plot_test_on_vertex(vertex: int, filename: str):
    # читаємо данні з .csv
    column_names = ['vertex_count', 'percentage of density', 'time']
    df = pd.read_csv(filename, header=None, names=column_names)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    # рахуємо середнє значення
    mean_values = df.groupby('percentage of density')['time'].mean()

    ax.plot(df['percentage of density'], df['time'], 'o', alpha=0.5, color='green')
    ax.plot(mean_values.index, mean_values.values, color='orange', linewidth=3, label='Середній час')


    ax.set_title(f'Dependence of time on density in {vertex} vertex', fontsize=14)
    ax.set_ylabel('Time')
    ax.set_xlabel('Density')
    ax.grid(True)
    ax.legend()


    # зберігаємо графік
    plt.savefig(f'tests_vertex/plot_{vertex}.png')
    plt.show()
    plt.close()


def test_on_vertex():
    print()
    vertex = input_to_int("On what number of vertices will we make the test(20 to 200): ", min_value= 20, max_value= 200)

    filename = f'tests_vertex/test_{vertex}.csv'
    for density in range(10, 100, 10):
        density /= 100

        for _ in range(20):
            test_time = time_tracker(vertex, density)

            with open(f"{filename}", "a") as file:
                to_append = f"{vertex}, {density}, {test_time:10f}\n"
                file.write(to_append)

    print("Test finished")
    print(f"Now yon can see your results in directory {filename}")

    print(f"Generating plot")
    print(f"{RED}ТО MOVE FURTHER FIRST CLOSE PLOT WINDOW{RESET}")
    plot_test_on_vertex(vertex, filename)


def test_on_density():
    print()
    density = input_to_int("On what persent of density will we make the test(0 to 100): ", min_value=0, max_value=100)

    filename = f'tests_density/test_{density}.csv'

    for vertex in range(20, 201, 10):

        for _ in range(20):
            test_time = time_tracker(vertex, density)

            with open(f"{filename}", "a") as file:
                to_append = f"{vertex}, {density}, {test_time:10f}\n"
                file.write(to_append)

    print("Test finished")
    print(f"Now yon can see your results in directory {filename}")

    print(f"Generating plot")
    print(f"{RED}ТО MOVE FURTHER FIRST CLOSE PLOT WINDOW{RESET}")
    plot_test_on_density(density, filename)



    print()


def plot_test_on_density(density, filename):
    # читаємо данні з .csv
    column_names = ['vertex_count', 'percentage of density', 'time']
    df = pd.read_csv(filename, header=None, names=column_names)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    # рахуємо середнє значення
    mean_values = df.groupby('percentage of density')['time'].mean()

    # Побудова: X = df['percentage of density'], Y = df['time']
    ax.plot(df['vertex_count'], df['time'], 'o', alpha=0.5, color='green')
    ax.plot(mean_values.index, mean_values.values, color='orange', linewidth=3, label='Середній час')

    ax.set_title(f'Dependence of time on {density}% density', fontsize=20)

    ax.set_ylabel('Time')
    ax.set_xlabel('Vertex')

    ax.grid(True)
    ax.legend()

    # зберігаємо графік
    plt.savefig(f'tests_vertex/plot_{density}.png')
    plt.show()
    plt.close()


def test_parameters():

    while True:
        choice = lst_input_to_int(["Test on number of vertex", "Test on density", "Quit"])
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

    print("Start testing")
    for vertex in range(20, 201, 10):

        with open(f"tests_all/test_{vertex}.csv", "w") as file:
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
                test_time = time_tracker(vertex, density)

                with open(f"tests_all/test_{vertex}.csv", "a") as file:
                    to_append = f"{vertex}, {density}, {test_time:10f}\n"
                    file.write(to_append)
    print("\nFinish testing")
    print("Now yon can see your results in directory tests_all/")