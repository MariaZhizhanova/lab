```python
with open("input.txt", "r") as file:
    content = file.read()

words = content.split()

word_count = {}

for word in words:
    word = word.strip('.,!?()[]{}"\'').lower()
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)

print("Количество слов в тексте:", len(words))
print("Самое часто встречающееся слово:", most_common_word)
```
