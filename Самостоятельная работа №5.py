### day.py

```python
def square_triangle(a, b, c):
p = (a + b + c) / 2
return (p * (p - a) * (p - b) * (p - c)) ** 0,5
```
### day.py

### main.py

```python
def square_triangle(a, b, c):
p = (a + b + c) / 2
return (p * (p - a) * (p - b) * (p - c)) ** 0,54

from main import square_triangle

a = int(input("Enter a > 0: "))
b = int(input("Enter b > 0: "))
c = int(input("Enter c > 0: "))

if a <=0 or b or c <= 0:
    print("Fatal error, arguments must be greater than 0")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Fatal error, there's no triangle")
else:
    square = square_triangle(a, b, c)
    print(f"Square of the triangle is {fround(square, 3)}")
```
