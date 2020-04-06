# Task 1
print('***')
print('Task 1: методами строк очистить текст от знаков препинания')
import re
read_txt = open('text.txt', 'r', encoding='UTF-8')
text = read_txt.read()
change_items = text.replace('-', ' ')
finish_txt = re.sub(r'[^\w\s]','',change_items)
print(finish_txt)

# Task 2
print('***')
print("Task 2: сформировать list со словами (split)")
create_list = finish_txt.split()
print(create_list)

# Task 3.1
print('***')
print("Task 3: привести все слова к нижнему регистру (map)")
low_leaters_txt = list(map(lambda x:x.lower(), create_list))
print(low_leaters_txt)

# Task 3.2
print('***')
print("Task 3: получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте")
dictionary={a:low_leaters_txt.count(a) for a in low_leaters_txt}
import operator
x = dictionary
dictionary = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print(dictionary)

# Task 4
print('***')
print('Task4: вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')

for i in range(5):
    print(dictionary[i])
print('Всего уникальных слов: ', len(set(dictionary)))
