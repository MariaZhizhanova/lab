```python
def find_most_common_numbers(input_string):
    number_count = {}

    for char in input_string:
        if char.isdigit():
            number = int(char)
            number_count[number] = number_count.get(number, 0) + 1
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1], reverse=True)
    top_three_numbers = sorted_numbers[:3]
    top_three_numbers = sorted(top_three_numbers, key=lambda x: x[0])
    result_dict = {number: count for number, count in top_three_numbers}
    
    return result_dict
input_string = "98123756984012345"
result = find_most_common_numbers(input_string)
print(result)
for number, count in result.items():
    print(f"Число {number}: {count} раз")
```
