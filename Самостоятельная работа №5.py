```python
def создать_множество(список):
    уникальные_элементы = set(список)
    результат = set()
    
    for элемент in уникальные_элементы:
        количество = список.count(элемент)
        if количество > 1:
            результат. add (элемент)
            for повтор in range(2, количество + 1): 
                строка = str(элемент) * повтор 
                результат. add (строка)
        else:
            результат. add (элемент)
            
            
    return результат

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

результат_1 = создать_множество(list_1)
результат_2 = создать_множество(list_2)
результат_3 = создать_множество(list_3)

print(результат_1)
print(результат_2)
print(результат_3)
```
