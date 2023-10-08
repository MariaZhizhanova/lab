```python
def read_file (f_name):
    try:
        with open("пустой_файл.txt", "r") as file:
            f = file.read()
            if not f:
                raise Exception("Файл пустой")
            else:
                print(f)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as ex:
         print(ex)
f_name = "file.txt"
read_file(f_name)
```
