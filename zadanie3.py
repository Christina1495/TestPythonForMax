import re
from collections import Counter

text = input("Введите текст для подсчета слов: ")
if text == "":
    print("К сожалению, вы не ввели текст в консоли, поэтому текст будет загружен из файла!")
    document_text = open('text.txt', 'r')
    text = document_text.read()
    print(text)
else:
    print("Текст успешно считан с консоли, результат:")
array_text = re.split(r'\W+', text.lower())
# удаление пустого символа в конце
array_text.remove('')
print("Слов в тексте - {0} \nКажое слово входит:".format(len(array_text)))
text_counts = Counter(array_text)
for words in text_counts:
    print("{0} - {1} ".format(words, text_counts[words]))

