""" 
    Words frequency counter
"""

text = input('Enter the sentences:').lower()
words = text.split()

words_count = {}


for word in words:
    words_count[word] = words_count.get(word, 0) + 1


print('\nWords Frequency Counter')
for word, count in words_count.items():
    print(f'{word}:{count}')
