### 1) Выведите длину предложения.

```python
str = (input("Введите предложение: "))
print(len(str))
```
### 2) Переведите предложение в нижний регистр.

```python
print(str.lower())
```
### 3) Подсчитайте количество гласных (a, e, i, o, u) в предложении.

```python
vowels = [char for char in str.lower() if char in "aeiou"]
count = len(vowels)

print("Количество гласных букв:", count)

### 4) Замените все слова "ugly" на "beauty"

```python
new_s = str.lower().replace('ugly', 'beauty')
print(new_s) 
```
### 5)Проверьте, начинается ли предложение с "The" и заканчивается ли на "end"

```python
result = str.lower().startswith("the")
result_2 = str.lower().endswith("end")
 
print(result)
print(result_2)
```
