```python
def calculate_average_grades(students):
    average_grades = []
    
    for student in students:
        name, grades = student
        if not grades:
            average = 0.0
        else:
            total_grade = sum(grade for subject, grade in grades)
            average = total_grade / len(grades)
        
        average_grades.append((name, average))
    
    return average_grades

students = [
    ("Иван", [("История", 4), ("Литература", 5), ("Физика", 3)]),
    ("Александр", [("История", 5), ("Литература", 4), ("Физика", 4)]),
    ("Мария", [("История", 3), ("Литература", 5), ("Физика", 5)]),
]

average_grades = calculate_average_grades(students)
print(average_grades)
```
