```python
from datetime import datetime
from math import sqrt

def main(**kwargs):
    # Итерируемся по переданным ключ-значение аргументам
    for key, value in kwargs.items():
        # Вычисляем гипотенузу прямоугольного треугольника с заданными катетами
        result = sqrt(value[0] ** 2 + value[1] ** 2) 
        # Выводим результат
        print(result)

if __name__ == '__main__':
    # Засекаем время начала выполнения программы
    start_time = datetime.now()
    
    # Вызываем функцию main с передачей словаря аргументов
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    
    # Вычисляем время, затраченное на выполнение программы
    time_costs = datetime.now() - start_time
    # Выводим время выполнения
    print(f"Время выполнения программы - {time_costs}")

```

