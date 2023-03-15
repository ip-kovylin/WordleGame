import random

dic_sort = []
dic_sort_5 = []
with open('russian.txt', 'r', encoding="windows-1251") as dic_:
    for line in dic_:
        dic_sort.append(line.rstrip('\n'))
    for word in dic_sort:
        if len(word) == 5:
            dic_sort_5.append(word)
word = random.choice(dic_sort_5)
list_word = []
for i in word:
    list_word.append(i)


def inp_check(x):
    x_list = []
    if x in dic_sort_5:
        for w in x:
            x_list.append(w)
        return x_list
    else:
        return False


def game():
    count = 5
    open_wrd = ['*', '*', '*', '*', '*']
    ex_letter = []
    no_letter = []

    while count != 0:
        list_try_word = []
        try_word = str(input('Введите слово:  '))

        if inp_check(try_word):
            pass
        else:
            print('Введены некорректные данные. Введите слово из 5 букв')
            continue

        for n in try_word:
            list_try_word.append(n.lower())

        for v in range(5):
            if list_try_word[v] in list_word and list_try_word[v] not in ex_letter:
                ex_letter.append(list_try_word[v])
            if list_try_word[v] not in list_word and list_try_word[v] not in no_letter:
                no_letter.append(list_try_word[v])
            if list_try_word[v] == list_word[v]:
                open_wrd[v] = list_try_word[v]
            else:
                pass

        if list_try_word != open_wrd:
            count -= 1
            print(' '.join(open_wrd).upper())
            if len(ex_letter):
                print('В слове ЕСТЬ:', ', '.join(ex_letter).upper())
            print('В слове НЕТ:', ', '.join(no_letter).upper())
            print(f'Попыток осталось: {count}')
        else:
            return f'Победа! Загаданное слово: {word.upper()}'

    return f'Проигрыш! Вы не отгадали слово: {word.upper()}'


print(game())
