def are_triangle_points_collinear(
        first_x: int,
        first_y: int,
        second_x: int,
        second_y: int,
        third_x: int,
        third_y: int
) -> bool:
    return (second_x - first_x) * (third_y - first_y) - (third_x - first_x) * (second_y - first_y) == 0
