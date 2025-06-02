# ✳️ Подвиг 1  
def get_sq(num: float) -> float:
    return num * num

val = float(input("Введите число для возведения в квадрат: "))
print(get_sq(val))   


# ✳️ Подвиг 2  
def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a

 


# ✳️ Подвиг 4  
def is_even(x: int) -> bool:
    return x % 2 == 0

 
while True:
    x = int(input("Введите целое число (1 — выход): "))
    if x == 1:
        break
    if is_even(x):
        print(x)


# ✳️ Подвиг 6  
tp = input("Введите RECT для прямоугольника или что-то другое для квадрата: ").strip()

if tp == "RECT":
    def get_sq(a: float, b: float) -> float:
        return a * b
else:
    def get_sq(a: float) -> float:
        return a * a

 


# ✳️ Подвиг 8  
def city_info(city_name: str) -> tuple[str, int]:
    return (city_name, len(city_name))

 
cities_input = input("Введите названия городов через пробел: ")
cities = cities_input.strip().split()
 
 
d = {name: length for name, length in (city_info(c) for c in cities)}

 
for city in sorted(d, key=lambda c: d[c]):
    print(f"{city}: {d[city]}")