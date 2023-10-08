```python
def fib(n):
    a, b = 1, 1

    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(str(a) + "\n")
            a, b = b, a + b

fib(200)
```
