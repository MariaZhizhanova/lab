```python
with open('input.txt', 'r') as file:
    forbidden_words = file.read().split()

sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

words = sentence.split()

def censor_word(word):
    return '*' * len(word)

censored_sentence = ' '.join(censor_word(word.lower()) if word.lower() in forbidden_words else word for word in words)

print(censored_sentence)
```
