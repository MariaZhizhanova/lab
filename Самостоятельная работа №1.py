```python
x = input("Введите последовательность чисел, разделенных пробелом: ")
числа = list(map(int, x.split()))

список_данных = числа
кортеж_данных = tuple(числа)

print("Список данных:", список_данных)
print("Кортеж данных:", кортеж_данных)
```
