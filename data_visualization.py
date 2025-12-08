import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import os

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

def search_global_maximum() -> float:
    """
    шукає найвище значення часу з усіх файлів

    :return: y_limit це найвище значення часу зі всіх файлів
    """
    global_max_time = 0

    # проходимось по кожному файлу, щоб отримати максимальне значення
    print("Analyzing files to find maximum time...")
    for test_number in range(20, 201, 10):

        filename = f'tests_all/test_{test_number}.csv'

        # якщо не існує такого файлу, то пишемо що не існує
        if not os.path.exists(filename):
            print(f"File {filename} not found, skip")
            continue


        data_frame = pd.read_csv(filename)

        # Знаходимо макс. час у цьому файлі
        current_max = data_frame['time'].max()

        # якщо локальний максимум файла більший за глобальний максимум, то перезаписуємо глобальний
        if current_max > global_max_time:
            global_max_time = current_max


    print(f"Глобальний максимум часу знайдено: {global_max_time}")

    # Додамо трохи простору зверху (наприклад, +10%), щоб точки не впиралися в стелю
    y_limit = global_max_time * 1.1

    return y_limit


def visualization():
    """
    створює графіки

    :return: None
    """

    y_limit = search_global_maximum()

    for vertex in range(20, 201, 10):

        filename = f'tests_all/test_{vertex}.csv'
        print(f'open {filename}')

        # якщо не існує такого файлу, то пишемо що не існує
        if not os.path.exists(filename):
            print(f"File {filename} not found, skip")
            continue

        # читаємо данні з .csv
        df = pd.read_csv(filename)

        # Створюємо фігуру з ДВОМА "вікнами" (1 рядок, 2 колонки)
        # figsize робимо ширшим (16, 6)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))


        # --- ГРАФІК 1: Глобальний масштаб (для порівняння) ---
        ax1.plot(df['percentage of density'], df['time'], 'o', alpha=0.5, color='blue')

        # рахуємо середнє значення
        mean_values = df.groupby('percentage of density')['time'].mean()
        # Малюємо лінію середніх значень
        # mean_values.index — це щільність (X), mean_values.values — це середній час (Y)
        ax1.plot(mean_values.index, mean_values.values, color='skyblue', linewidth=3)

        ax1.set_ylim(0, y_limit)  # <--- ФІКСОВАНИЙ ЛІМІТ
        ax1.set_title(f'Масштаб: Глобальний (Max={y_limit:.5f})')
        ax1.set_ylabel('Час')
        ax1.set_xlabel('Щільність')
        ax1.grid(True)


        # --- ГРАФІК 2: Локальний масштаб (для деталей) ---
        ax2.plot(df['percentage of density'], df['time'], 'o', alpha=0.5, color='green')
        ax2.plot(mean_values.index, mean_values.values, color='orange', linewidth=3)

        # ТУТ НЕМАЄ set_ylim, тому масштаб підлаштується під конкретний файл
        ax2.set_title(f'Масштаб: Локальний (Деталі {vertex} вершин)')
        ax2.set_xlabel('Щільність')
        ax2.grid(True)


        # Загальний заголовок для всієї картинки
        fig.suptitle(f'Аналіз для {vertex} вершин', fontsize=16)

        # зберігаємо графік
        plt.savefig(f'tests_all/plot_{vertex}.png')

        # Важливо: закриваємо фігуру, щоб очистити пам'ять,
        # інакше після 20 графіків комп'ютер може почати гальмувати
        plt.close()

    print("Finish!")


def get_stats():
    pd.set_option('display.float_format', '{:.8f}'.format)

    results = {}
    for vertex in range(20, 201, 10):

        df = pd.read_csv(f"tests_all/test_{vertex}.csv")

        df_max_density = df[df['percentage of density'] == 0.9]
        average_time_at_max_density = df_max_density['time'].mean()

        k = average_time_at_max_density / 0.9
        results[vertex] = k

    for vertex, k_value in results.items():

        formatted_k = f"{k_value:.18f}"
        print(formatted_k)

    vertices = list(results.keys())  # Ключі: Кількість вершин (X)
    coefficients = list(results.values())  # Значення: Коефіцієнт k (Y)

    ## 2. Створюємо графік 📈
    plt.figure(figsize=(10, 6))  # Створюємо нову фігуру

    # Побудова графіка:
    # Використовуємо .plot() для створення лінії, 'o' - додаємо маркери
    plt.plot(vertices, coefficients, marker='o', linestyle='-', color='blue', label='Коефіцієнт k')

    ## 3. Налаштування осей та заголовків
    plt.title('Залежність коефіцієнта k від кількості вершин')
    plt.xlabel('Кількість вершин (Vertex)')
    plt.ylabel('Коефіцієнт k (Середній час / 0.9)')

    # Додаємо сітку для кращої читабельності
    plt.grid(True, linestyle='--', alpha=0.7)

    # Додаємо легенду (опис того, що відображає лінія)
    plt.legend()

    plt.show()


    plt.savefig('coefficient_vertices.png')
    plt.close()


# visualization()
# get_stats()


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
    plt.savefig(f'tests_density/plot_{density}.png')
    plt.show()
    plt.close()


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