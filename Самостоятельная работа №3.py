```python
import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_one = max(one)
min_one = min(one)
max_two = max(two)
min_two = min(two)
max_three = max(three)
min_three = min(three)

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area1 = calculate_triangle_area(max_one, max_two, max_three)
area2 = calculate_triangle_area(min_one, min_two, min_three)

print("Площадь треугольника, составленного из максимальных элементов:", area1)
print("Площадь треугольника, составленного из минимальных элементов:", area2)
```
