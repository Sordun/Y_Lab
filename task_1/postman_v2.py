def get_path_with_two_points(point_1: tuple, point_2: tuple) -> float:
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def calculate_path_rec(
    first_point: tuple,
    last_point: tuple,
    data: list,
    result: list,
    result_path_size: float,
):
    if len(data) == 0:
        path_size = get_path_with_two_points(
            last_point,
            first_point,
        )
        result.append((first_point, path_size))
        result_path_size += path_size
        return result_path_size, result
    else:
        point_path_data = []
        for index, point in enumerate(data):
            path_size = get_path_with_two_points(
                last_point,
                point,
            )
            point_path_data.append(
                calculate_path_rec(
                    first_point,
                    point,
                    data[:index] + data[index + 1 :],
                    result + [(point, path_size)],
                    result_path_size + path_size,
                )
            )

        return min(point_path_data, key=lambda t: t[0])


def calculate_and_print_path(data: list):
    result = calculate_path_rec(
        data[0],
        data[0],
        data[1:],
        [],
        0,
    )

    print(f"{data[0]}", end="")
    path_full_size = 0
    for point, path_size in result[1]:
        path_full_size += path_size
        print(f" -> {point}[{path_full_size}]", end="")

    print(f" = {result[0]}")


def main():
    data = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    calculate_and_print_path(data)


if __name__ == "__main__":
    main()
