#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_str = 'Напишите прогабврааааамму, удабваляющую из текста все слова, содержащие'
my_str = my_str.split(' ')
res = ''
for word in my_str:
    if word.find('абв') == -1:
        res += word + ' '
print(res)


#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
#ход друг после друга. Первый ход определяется жеребьёвкой. За один 
#ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
#сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы 
#забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""


print('Условие игры: '
'На столе лежит 2021 конфета.'
'Играют два игрока делая ход друг после друга. '
'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
'Все конфеты оппонента достаются сделавшему последний ход.\n')


def play_game(kolichestvo, players, kolichestvo_candies):
    count = 0
    while kolichestvo > 0:
        print(f'{players[count%2]}, Ваш ход, сколько конфет возьмете?\n')
        candy = int(input())
        print('----------------------------------------------')
        if candy < 0 or candy > kolichestvo_candies or candy > kolichestvo:
            print(f'Конфет больше {kolichestvo_candies} брать нельзя, осталось конфет: {kolichestvo} шт.!')
        else: 
            kolichestvo = kolichestvo - candy
            print(f'Осталось конфет: {kolichestvo} шт.\n')
            if kolichestvo > 0: print('Ход следующего игрока\n')
            else: print("Game over!\n")
        count +=1
    return players[not count%2]


player_1 = input('Введите имя первого игрока: \n')
player_2 = input('Введите имя второго игрока: \n')

kolichestvo = int(input('Введите количество конфет, которое лежит на столе!\n'))
kolichestvo_candies = int(input('Введите количество конфет, которое можно взять за один ход!\n'))

players = [player_1, player_2]

winer = play_game(kolichestvo, players, kolichestvo_candies)
print(f'Поздравляем!!!!! Победителем стал {winer}! Он получает все конфеты!')


## Игра с ботом

from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
            'Основные правила игры: '
            'Нам будет дано некоторое количество конфет, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы с вами договоримся. '
            'Итак, начнём!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
    

    
#Создайте программу для игры в ""Крестики-нолики"". 

    


print('*'*100)
print('\n')
print('А теперь давайте сыграем в крестики нолики!')

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

# design_board(board)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуй')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
        design_board(board)
game(board)
    


#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



with open('next2.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('next2.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)


def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle_encode(my_text)

with open('next.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)
