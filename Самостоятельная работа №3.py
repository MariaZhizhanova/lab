```python
def add_two():
    user_input = input("Введите число: ")
    try:
        number = float(user_input)
        return 2 + number
    except (ValueError, TypeError):
        raise ValueError("Неподходящий тип данных.")
try:
    result = add_two()
    print(result)
except ValueError as e:
    print(e)
```
