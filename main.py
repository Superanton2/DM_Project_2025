import time

from Algorithm import topological_sort_matrix, topological_sort_list
from graph_generator import graph_generator, get_vertex
from helper_function import print_start, lst_input_to_int, input_to_int, BLUE, RESET, RED
from tester import test_parameters, test_all, print_single_test


def tester():
    while True:
        print()
        print(f"{BLUE}Now you can test algorithm on different tests{RESET}")

        choice = lst_input_to_int(["Test particular parameters", "Test All", "Quit"])
        if choice == 1:
            test_parameters()
        elif choice == 2:
            test_all()
        else:
            break




def demonstration():
    while True:
        print()
        print(f"{BLUE}Now you can interact with algorithm directly{RESET}")

        vertex = input_to_int("Say number of vertexes(20 to 200): ", min_value=20, max_value=200)
        density = input_to_int("Say density in % (0 to 100): ", min_value=0, max_value=100)
        density /= 100

        lst_of_graphs, adj_lst = graph_generator(vertex, density)

        vertex = get_vertex(lst_of_graphs)

        # Start the stopwatch / counter
        time_start = time.perf_counter()

        # алгоритм
        result = topological_sort_matrix(lst_of_graphs, vertex)

        # Stop the stopwatch / counter
        time_stop = time.perf_counter()
        total_time = time_stop - time_start

        normal_vertex = [item for item in vertex.keys()]
        print()
        print(f"Arguments:")
        print(f"  vertex = {normal_vertex}")
        print(f"  density = {density*100}%")
        print(f"Stats:")
        print(f"  result = {result}")
        print(f"  time = {total_time: 10}")
        print()

        print(f"Generating plot")
        print(f"{RED}ТО MOVE FURTHER FIRST CLOSE PLOT WINDOW{RESET}")
        print_single_test(lst_of_graphs, vertex)

        choice = lst_input_to_int(["Continue", "Quit"])
        if choice == 1:
            continue
        else:
            break

    return

  
def main():

    while True:
        print_start()

        print(f"{BLUE}Main {RESET}")
        choice = lst_input_to_int(["Play on your own", "Testing", "Quit"])

        if choice == 1:
            demonstration()
        elif choice == 2:
            tester()
        else:
            break
    print("Thanks for coming")

if __name__ == '__main__':
    main()