```python
with open('input.txt', 'r') as file:
    text = file.read()

letters_count = sum(c.isalpha() for c in text)
words_count = len(text.split())
lines_count = text.count('\n') + 1

print(f"Input file contains:")
print(f"{letters_count} letters")
print(f"{words_count} words")
print(f"{lines_count} lines")
```
