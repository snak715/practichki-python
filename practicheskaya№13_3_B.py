current = input('Имя исходного файла')
new = input('Имя нового файла')

numb = input("Введите цифру для приписывания: ")

with open(current, 'r') as input, 
     open(new, 'w') as output:
    
    for line in input:

        number = line.strip()
        
        new_number = number + numb
        
        output.write(new_number + '\n')

print(f"Новый файл '{new}' создан с приписанными цифрами.")
