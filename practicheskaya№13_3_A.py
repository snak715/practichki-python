filet = input('Введите имя файла : ')  
word1 = input("Введите первое слово : ")
word2 = input("Введите второе слово : ")

with open(filet, 'r') as file:
    text = file.read()

count_word1 = text.count(word1)
count_word2 = text.count(word2)

combined_word = f"{word1} {word2}"
count_combined = text.count(combined_word)

print(f"Слово '{word1}' встречается {count_word1} раз.")
print(f"Слово '{word2}' встречается {count_word2} раз.")
print(f"Слова '{word1}' и '{word2}' расположены друг за другом {count_combined} раз.")
