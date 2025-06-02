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
