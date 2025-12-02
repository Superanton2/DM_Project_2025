import matplotlib.pyplot as plt
import pandas as pd
import os

def search_global_maximum() -> float:
    """
    шукає найвище значення часу з усіх файлів

    :return: y_limit це найвище значення часу зі всіх файлів
    """
    global_max_time = 0

    # проходимось по кожному файлу, щоб отримати максимальне значення
    print("Analyzing files to find maximum time...")
    for test_number in range(20, 201, 10):

        filename = f'tests/test_{test_number}.csv'

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

        filename = f'tests/test_{vertex}.csv'
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
        plt.savefig(f'tests/plot_{vertex}.png')

        # Важливо: закриваємо фігуру, щоб очистити пам'ять,
        # інакше після 20 графіків комп'ютер може почати гальмувати
        plt.close()

    print("Finish!")

visualization()