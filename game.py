import random

dic_sort = []
dic_sort_5 = []
with open('russian.txt', 'r') as dic_:
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
    if x in dic_sort_5:
        pass
    else:
        return False

    # if len(x) != 5:
    #     return False
    # else:
    #     pass

    x_list = []
    x_int = []
    for i in x:
        x_list.append(i)
    for j in x_list:
        try:
            j == int(j)
        except ValueError:''
        else:
            return False
    return x_list

def game():
    count = 5
    open_wrd = ['*', '*', '*', '*', '*']
    while count != 0:
        list_try_word = []
        try_word = str(input('Введите слово из 5 букв:  '))

        # if try_word == word:
        #     return 'Победа!'
        # else:
        #     pass

        if inp_check(try_word):
            pass
        else:
            print('Введены некорректные данные. Введите слово из 5 букв')
            continue

        for i in try_word:
            list_try_word.append(i.lower())

        for i in range(5):
            if list_try_word[i] == list_word[i]:
                open_wrd[i] = list_try_word[i]
            else:
                pass

        if list_try_word != open_wrd:
            count -= 1
            print(' '.join(open_wrd).upper(), f'Попыток осталось: {count}', sep='\n')
        else:
            count = 0
            return 'Победа!'

    return f'Проигрыш! Вы не отгадали слово: {word.upper()}'


print(game())
