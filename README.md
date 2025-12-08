# DM_Project_2025
Це репозиторія для проєкту з дискретної математики(MATH115). 
Цей проєкт написайни на Python з використанням [matplotlib](https://github.com/matplotlib/matplotlib), [networkx](https://github.com/networkx/networkx), 
[pandas](https://github.com/pandas-dev/pandas).
Додаткова інформація по реалізації проєкту знаходиться у [гугл документi](https://docs.google.com/document/d/1NpEg4FQb0rTt3JI4L8anyVpce2HQUAiGS4nFT-Sv94Q/edit?usp=sharing)

## Інформація
Тема: **Алгоритм топологічного сортування на основі DFS.**  
Автори:
  - [Anton Fedoriv](https://github.com/Superanton2)  
  - [Andrew Korzh](https://github.com/clafish)  
  - [Kateryna Sadovska](https://github.com/Shlyapkas)


Документ: [гугл документ](https://docs.google.com/document/d/1NpEg4FQb0rTt3JI4L8anyVpce2HQUAiGS4nFT-Sv94Q/edit?usp=sharing)

## Getting Started

Дотримуйтесь цих інструкцій, щоб запустити копію проекту на локальній машині.

### Prerequisites
- Python 3.6+
- Pip (Python package installer)

### Installation

1.  **Клонуйте репозиторій:**
    ```bash
    git clone https://github.com/Superanton2/DM_Project_2025.git
    cd DM_Project_2025
    ```

2.  **Встановіть необхідні пакети Python:**
    ```bash
    pip install -r /requirements.txt
    ```


## Тестування  

Графік часу роботи алгористу в залежності від параметрів кількості вершин та густини. 
> [!CAUTION]
> !!!ВАЖЛИВО!!! час приблизний, оскільки він буде залежити від потужності центрального процесора !!!ВАЖЛИВО!!!

<a href="url"><img src="https://github.com/Superanton2/DM_Project_2025/blob/main/photos/main_graph.png" align="left" height="350"></a>  



**Структура проєкту**
```
.
├── tests_all/             # данні загальних тестів
├── tests_density/         # данні з фіксованою густиною
├── tests_vertex/          # данні з фіксованою кількість вершин
│
├── graph_generator.py     # генератор графів
├── Algorithm.py           # алгоритм топологічного сортування
├── tester.py              # модуль тестування
├── data_visualization.py  # функції для візуалізації данних
├── main.py                # головний файл який керує всім
│
├── helper_function.py     # допоміжні функції для зручної роботи
├── requirements.txt       # потрійбні налаштування
└── README.md              # Цей файл
```
