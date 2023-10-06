```python
import os


def main():
    expenses = load_expenses()

    while True:
        print("Учет расходов")
        print("1. Ввести новый расход")
        print("2. Показать все расходы")
        print("3. Выход")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    return []


def add_expense(expenses):
    expense = input("Введите расход: ")
    expenses.append(expense)
    print("Расход успешно добавлен.")


def show_expenses(expenses):
    if expenses:
        print("Список расходов:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense}")
    else:
        print("Список расходов пуст.")


def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense}\n")


if __name__ == "__main__":
    main()
```
