from random import choices
name = open('Names.txt', 'r', encoding='UTF-8')
list_names = name.read().split()
# print(list_names)
def choice_name(names, length_list):
    return choices(names, k=length_list)
task_list = sorted(choice_name(list_names, length_list = 100))

def most_frequently_name (names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]

def most_frequently_leatter(names):
    letters = []
    counts = []
    for i in range(len(names)): #извлекаем из имён буквы
        names[i] = names[i][0]
        if not (names[i] in letters):
            letters.append(names[i])
    for i in range(len(letters)): #считаем сколько раз каждая буква встречается
        counts.append(names.count(letters[i]))
    #print(letters) #проверка букв
    #print(counts) #проверка их количества
    return letters[counts.index(max(counts))] #возвращаем букву, которая чаще всего встречалась

print('Light_1:')
print(task_list)
print('Light_2:')
print(most_frequently_name(list_names))
print('Light_3:')
print (most_frequently_leatter(list_names))

