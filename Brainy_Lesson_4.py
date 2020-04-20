from random import choices
name = open('Names.txt', 'r', encoding='UTF-8')
list_names = name.read().split()
# print(list_names)
def choice_name(names, length_list):
    return choices(names, k=length_list)
task_list = sorted(choice_name(list_names, length_list = 100))

def most_frequently (names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]

print('Light_1:')
print(task_list)
print('Light_2:')
print(most_frequently(list_names))
print('Light_3:')



