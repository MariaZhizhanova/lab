```python
class Сотрудник:
    def __init__(self, имя, фамилия, должность, зарплата):
        self.имя = имя
        self.фамилия = фамилия
        self.должность = должность
        self.зарплата = зарплата

    def информация(self):
        return f"{self.имя} {self.фамилия}, {self.должность}, Зарплата: {self.зарплата} рублей в месяц"
        
сотрудник1 = Сотрудник("Иван", "Иванов", "Менеджер", 50000)
сотрудник2 = Сотрудник("Петр", "Петров", "Разработчик", 70000)

print(сотрудник1.информация())
print(сотрудник2.информация())
```
