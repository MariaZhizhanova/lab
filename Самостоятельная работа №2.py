```python
def remove_first_occurrence(tup, element):
    if element in tup:
        index = tup.index(element)
        new_tuple = tup[:index] + tup[index+1:]
        return new_tuple
    else:
        return tup

inputs = [((1, 2, 3), 1), ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3), ((2, 4, 6, 6, 4, 2), 9)]
expected_results = [(2, 3), (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), (2, 4, 6, 6, 4, 2)]

for i in range(len(inputs)):
    result = remove_first_occurrence(inputs[i][0], inputs[i][1])
    print(f"Входные данные: {inputs[i][0]}, элемент для удаления: {inputs[i][1]}")
    print(f"Результат: {result}")
    print(f"Ожидаемый результат: {expected_results[i]}\n")
```
