```python
class Сотрудник:
    def __init__(self, имя, фамилия, должность, зарплата):
        self.__имя = имя
        self.__фамилия = фамилия
        self.__должность = должность
        self.__зарплата = зарплата
        self.__проекты = []

    def информация(self):
        return f"{self.__имя} {self.__фамилия}, {self.__должность}, Зарплата: {self.__зарплата} рублей в месяц"

    def добавить_проект(self, проект):
        self.__проекты.append(проект)
        return f"Проект '{проект}' добавлен для {self.__имя} {self.__фамилия}"

class Руководитель(Сотрудник):
    def __init__(self, имя, фамилия, должность, зарплата, подчиненные=None):
        super().__init__(имя, фамилия, должность, зарплата)
        self.__подчиненные = подчиненные or []

    def добавить_подчиненного(self, подчиненный):
        self.__подчиненные.append(подчиненный)
        return f"{подчиненный.имя} {подчиненный.фамилия} добавлен(а) в список подчиненных для {self.__имя} {self.__фамилия}"

сотрудник1 = Сотрудник("Иван", "Иванов", "Менеджер", 50000)
сотрудник2 = Сотрудник("Петр", "Петров", "Разработчик", 70000)

руководитель1 = Руководитель("Анна", "Иванова", "Руководитель отдела", 80000)
сотрудник3 = Сотрудник("Мария", "Сидорова", "Ассистент", 40000)

print(сотрудник1.добавить_проект("Проект 1"))
print(сотрудник2.добавить_проект("Проект 2"))

print(сотрудник1.информация())
print(сотрудник2.информация())

print(руководитель1.добавить_проект("Проект 3"))
print(руководитель1.добавить_подчиненного(сотрудник3))
```
