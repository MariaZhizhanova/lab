```python
def extract_employee_data(data, employee_id):
    if employee_id not in data:
        return tuple()  
    
    start_index = data.index(employee_id)
    end_index = data[::-1].index(employee_id) 
    end_index = len(data) - end_index  
    
    return data[start_index:end_index + 1]

inputs = [((1, 2, 3), 8), ((1, 8, 3, 4, 8, 8, 9, 2), 8), ((1, 2, 5, 1, 2,), 8)]
expected_results = [(), (8, 3, 4, 8), (8, 5, 1, 2, 9)]

for i in range(len(inputs)):
    result = extract_employee_data(inputs[i][0], inputs[i][1])
    print(f"Входные данные: {inputs[i][0]}, идентификатор сотрудника: {inputs[i][1]}")
    print(f"Ожидаемый результат: {expected_results[i]}\n")
``
