# main_funcs.py

def get_sq(num: float) -> float:
    return num * num

def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a

def is_even(x: int) -> bool:
    return x % 2 == 0

def get_sq_rect(a: float, b: float) -> float:
    return a * b

def get_sq_square(a: float) -> float:
    return a * a

def city_info(city_name: str) -> tuple[str, int]:
    return (city_name, len(city_name))
