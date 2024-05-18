import random


def check(old, new):
    if old[len(old) - 1].capitalize() == new[0]:
        return True
    else:
        if old[len(old) - 1] == 'ь' and old[len(old) - 2].capitalize() == new[0]:
            return True
        else:
            return False

print('Ведется настройка программы. Пожалуйста, подождите...')
cilistfl = open('list', encoding='utf-8')
cilist = []
for a in cilistfl.readlines():
    if a != 'end':
        cilist.append(a[:len(a) - 1])
fcounter = 0
print(f'Вас приветствует программа для игры в города.')
print(f'Ваша задача - называть города мира, начинающиеся с конечной буквы указанных данной программой.')
print(f'Игра закончится, если вы допустите 3 ошибки. Удачи.')
curcit = random.choice(cilist)
print(f'Первый город - {curcit}')
cilist.remove(curcit)
while fcounter < 3:
    response = input()
    if check(curcit, response) and response in cilist:
        curcit = response
        cilist.remove(curcit)
        aichoice = random.choice(cilist)
        while not check(curcit, aichoice):
            aichoice = random.choice(cilist)
        curcit = aichoice
        print(curcit)
        cilist.remove(curcit)
    else:
        fcounter += 1
        print(f'Неверный ответ. Осталось попыток : {3 - fcounter}.')
print('Игра окончена!')