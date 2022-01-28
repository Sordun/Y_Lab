point_1 = (0, 2)  # Почтовое отделение – (0, 2)
point_2 = (2, 5)  # Ул. Грибоедова, 104/25 – (2, 5)
point_3 = (5, 2)  # Ул. Бейкер стрит, 221б – (5, 2)
point_4 = (6, 6)  # Ул. Большая Садовая, 302-бис – (6, 6)
point_5 = (8, 3)  # Вечнозелёная Аллея, 742 – (8, 3)

# пример подстановки значений в формулу
# ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

# маршрут
points = [(0, 2), (2, 5), (6, 6), (8, 3), (5, 2)]

# начальная точка
start_point = min(points)


def calculate_points(first_point: tuple, second_point: tuple) -> float:
    """Функция для вычисления расстояния между точками"""
    return (
        (second_point[0] - first_point[0]) ** 2
        + (second_point[1] - first_point[1]) ** 2
    ) ** 0.5


def finding_short_path():
    """Функция перебирает все точки и выводит путь"""
    calculated_points = 0
    last_point = 0
    print(start_point, end=" -> ")
    for current_point in range(len(points) - 1):
        last_point = current_point
        next_point = current_point + 1
        current_path = calculate_points(points[current_point], points[next_point])
        calculated_points += current_path
        print(f"{points[next_point]}[{calculated_points}]", end=" -> ")
    finish_point = calculated_points + calculate_points(
        points[last_point + 1], start_point
    )
    print(f"{start_point}, [{finish_point}] = {finish_point}")


finding_short_path()
