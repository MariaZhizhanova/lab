```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}\n")
            log_file.write(f"Результат: {result}\n")
        return result
    return wrapper

@log_function_call
def multiply(a, b):
    return a * b

@log_function_call
def add(a, b):
    return a + b

result1 = multiply(3, 4)
result2 = add(5, 7)

print(f"Результат умножения: {result1}")
print(f"Результат сложения: {result2}")
```
