# задание на строки
#string = input()
#string_new = list(string)
#string_new_second = []
#for letter in string
    #if letter == A or letter == O or letter == Y or letter == E or letter == U or letter == I or letter == i or letter == 'u' or letter == 'e' or letter == 'y' or letter == 'o' or letter == 'a'
        #continue
    #else
        #string_new_second.append(letter)
#string_new_second = '.'.join(string_new_second)
#string_new_third = string_new_second.lower()
#print('.'+ string_new_third)


#print('  ~~~ n ^ ^ n((__))n_''''_n(_)^(_)')


#word = input()
#print('Что вы сказали '+word+''+' Какое интересное слово')


#first_name = input()
#second_name = input()
#print('Здравствуйте,',second_name, first_name+'!')


#number = int(input())
#number_pred=str(number-1)
#number_sled=str(number+1)
#print('Для числа',number,'предыдущим будет число', number_pred+'.')
#print('Для числа',number,'следущим будет число', number_sled+'.')


#Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом,
# т.е. числом, которое одинаково читается слева направо и справа налево.
#stroka = input()
#print(stroka)
#stroka_list = list(stroka)
#if stroka_list[0]==stroka_list[3] and stroka_list[1]==stroka_list[2]
    #print('YES')
#else
    #print('NO')

#a=input()
#a = a.split()
#a_list = list(a)
#if int(a_list[0])+int(a_list[1]) == int(a_list[2])
    #print('YES')
    #print(f'{a_list[0]}+{a_list[1]}={int(a_list[0])+int(a_list[1])}')
#else
    #print('NO')
    #print(f'{a_list[0]}+{a_list[1]}={a_list[0] + a_list[1]}')


#string = input()
#reversed_string = string[-1]
#string_two = input()
#if string_two == reversed_string
    #print('YES')
#else
    #print('NO')

#import time
#from datetime import datetime
#import random
from time import sleep
#odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#for i in range(5)
        #right_this_minute = datetime.today().minute
        #if right_this_minute in odds
            #print('This minute seems a little odds')
        #else
           # print('Not an odd minute')
        #wait_time = random.randint(1,60)
        #time.sleep(wait_time)


#str = input()
#if len(str)  6
    #str = str.rjust(6,'0')
#str_list = list(str)
#if int(str_list[0])+int(str_list[1])+int(str_list[2])==int(str_list[3])+int(str_list[4])+int(str_list[5])
    #print('YES')
#else
    #print('NO')


#numbers = ['1','2','3','4','5','6','7','8','9']
#words = ['a','b','c','d','e','f','g','h']
#word1 = input()
#word2 = input()
#def color_finding(word)
    #word_list = list(word)
    #letter1 = word_list[0] # зафиксировали букву
    #letter2 = word_list[1] # зафиксировали цифру
    #index1 = words.index(letter1)# нашли индекс среди букв
    #index2 = numbers.index(letter2)# нашли индекс
    #if (int(index1)+int(index2))%2 == 0
        #color1 = 'Black'
    #else
        #color1 = 'White'
    #return(color1)
#if color_finding(word1)==color_finding(word2)
    #print('YES')
#else
    #print('NO')


#n = int(input())
#if n%2==0 # четное
    #print(f'{int(n2)}')
#elif n==1
    #print('-1')
#else
    #print(f'{int(-n2)-1}')


#a = int(input())
#b = int(input())
#if a==b
    #print('=')
#elif ab
    #print('')
#else
    #print('')


#a = int(input())
#b = int(input())
#c = int(input())
#if ab
#    if ac
#        print(a)
#    else
#        print(c)
#else
#    if bc
#        print(b)
#    else
#        print(c)


#n = int(input())# количество гостей
#if n == 1
    #print('0') # минимальное число кусков торта
#elif n%2==0
    #print(f'{int(n2)}')
#else
    #print(n)


#str = (input()).split()
#a,b,c = int(str[0]),int(str[1]),int(str[2])
#найдем максимум
#if ab
    #if ac
        #max = a
    #else
        #max = c
#else
    #if bc
        #max = b
    #else
        #max = c
#найдем минимум
#if ab
    #if ac
        #min = a
    #else
        #min = c
#else
    #if bc
        #min = b
    #else
        #min = c

#delta = int(max) - int(min)
#rint(delta)


#a = (input()).lower()
#b = (input()).lower()
#if ab
    #print('-1')
#elif ab
    #print('1')
#else
    #print('0')


#str =  list((input()).split())
#s = int(str[0])
#v1 = int(str[1])
#v2 = int(str[2])
#t1 = int(str[3])
#t2 = int(str[4])
#t_summ1 = t1 + (sv1) + t1
#t_summ2 = t2 + (sv2) + t2
#if t_summ1t_summ2
    #print('First')
#elif t_summ1t_summ2
    #print('Second')
#else
    #print('Friendship')


#str1 = list((input().lower()))
#str2 = list((input().lower()))
#if str1[-1] == 'ь'
    #if str1[-2]==str2[0]
        #print('Good')
    #else
        #print('Bad')
#else
    #if str1[-1]==str2[0]
        #print('Good')
    #else
        #print('Bad')

#flag1, flag2 = True, True
#number = int(input())
#if number%3==0 and number%5==0
    #print('FizzBuzz')
#elif number%3==0
        #print('Fizz')
#elif number%5==0
    #print('Buzz')
#else
    #print(number)


#a = int(input())
#b = int(input())
#c = int(input())
#if a == b and b == c
    #print('3')
#elif a == b or b==c or a==c
    #print('2')
#else
    #print('0')


#N = int(input())
#n=str(N)
#month = {'1''January',
#         '2''February',
#         '3''March',
#         '4''April',
#         '5''May',
#         '6''June',
#         '7''July',
#         '9''September',
#         '10''October',
#         '11''November',
#         '12''December'}
#print(month[n])


#age = int(input())
#if age12
#    if age=4
#        print('Ребенок')
#    elif age=2
#        print('Малыш')
#    else
#        print('Младенец')
#else
#    if age=65
#        print('Пожилой человек')
#    elif age=19
#        print('Взрослый человек')
#    else
#       print('Подросток')


#number1 = float(input())
#number2 = float(input())
#operation = input()
#known_operation = ['+','-','','']
#flag1=False
#if number2 == 0
#    flag1=True
#if operation not in known_operation
#    print('Неизвестно')
#else
#    if operation == '+'
#        print(number1+number2)
#    elif operation == '-'
#        print(number1-number2)
#    elif operation == ''
#        print(number1number2)
#    else
#        if operation == '' and flag1==True
#            print('Неизвестно')
#        elif operation == ''
#            print(number1number2)


#password = input()
#check_password = input()
#if len(password)7
    #print('Short')
#elif password == check_password
    #print('OK')
#else
    #print('Difference')


#k=6785
#while k194
#    if k%5==0
#        print(k)
#    k-=1

# изначально бобби больше лимана


#entered = list((input()).split())
#Limak,Bobby = int(entered[0]) , int(entered[1])
#k=0
#while int(Limak)=int(Bobby)
    #Limak=3
    #Bobby=2
    #k+= 1
#print(k)


#numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
#while 4 in numbers
    #numbers.remove(4)
#print(numbers)


#str = input()
#print(str)
#while len(str)0
#    print(str[1-11])
#    str = str[1-11]


#i=1
#N = int(input())
#while i2 = N
#    print(i2)
#    i+=1


#s = list((input()).split())
#X = int(s[0])
#Y = int(s[1])
#print(X,Y)
#n=1
#while XY
#    X=1.15
#    n+=1
#print(n)


#socks,mama_day = map(int,input().split())
#day = 0
#while socks0
#   socks-=1
#   day+=1
#   if day % mama_day == 0
#       print(f'мама пришла на {} день')
#       socks += 1
#print(day)


#time = 0
#a,b = map(int,input().split())
#while a0
#    a-=1
#    time+=1
#    if time % b == 0
#        a+=1
#print(time)


#i=0
#Flag = False
#Number = int(input())
#while Flag == False and 2i=Number
#    if Number == 2i
#        print(i)
#        Flag = True
#    i+=1
#if Flag == False
#    print('НЕТ')


#Пользователь вводит целые числа по одному в строке, последовательность оканчивается числом 0.
# Все, что вводится после 0 не относится к последовательности.
# Напишите программу, которая выводит сумму всех членов данной последовательности.
#sum = 0
#number = int(input())
#while number != 0
    #sum += number
    #number = int(input())
#print(sum)


#На каждой отдельной строчке пользователь вводит друг за другом пароли в виде строки символов.
# Валидными паролями будем считать строки, у которых длина варьируется от 5 до 9 символов включительно.
# Как только вы встретите первый невалидный пароль, ваша программа должна закончить считывать пароли и вывести последний введенный валидный пароль.
# Гарантируется, что первый пароль всегда валидный
#flag = True
#while flag == True
#    password = input()
#    if int(len(password))=9 and int(len(password))=5
#        flag = True
#        last_valid = password
#    else
#        flag = False
#print(last_valid)


#k=0
#sum = 0
#n = int(input()) # вместимость
#flag = True
#while flag == True
#    number = int(input())
#    if sum+number=n
#        sum += number
#        k+=1
#        flag = True
#    else
#        flag = False
#print('Довольно')
#print(sum)
#print(k)


# с 2000 до 0000, то есть 4 часа или 460=240 минут, от этого исходим
#a,b = map(int,input().split())# ввели количество задач и время, необходжимое чтобы добраться
#c = 1 # счетчик задач, которые успеем решить
#d = 240 - b -5 # вакантное время на решение задач
#while d=0
#    c += 1  # если все условия выполнены, увеличиваем счетчик
#    d = d - 5  c  # из свободного времени вычитаем время на i задачу
#if ca
#    print(a)
#else
#    print(c-1)


#n = int(input()) # количество кубиков
#level = 0
#cub_level = 0
#sum = 0
#while sumn
#    level+=1
#    cub_level+=level
#   sum+=cub_level
#if sum==n
#    print(level)
#else
#    print(level-1)


#n,m = map(int, input().split())
#a = list(map(int,input().split()))
#b = list(map(int,input().split()))
#i = j = 0
#c = []
#while i  n and j  m
#    if a[i]b[j]
#        c.append(a[i])
#        i+=1
#    else
#        c.append(b[j])
#        j+=1
#while in
#    c.append(a[i])
#    i+=1
#while jm
#    c.append(b[j])
#    j+=1
#for i in c
#    print(i, end = ' ')

#number = 1234567890
#count = 0
#while number  0
#    last_digit = number % 10
#    if last_digit  3
#        count = count + 1
#    number = number  10
#print(count)


#number = 73408
#m = 0
#s = 0
#while number  0
#    last_digit = number % 10
#    s = s + last_digit
#    if last_digit  m
#        m = last_digit
#    number = number  10
#print(s + m)


#Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.
#через for
#numb =  input()
#for i in reversed(numb)
#    print(i)
#через while
#numb =  int(input())
#while numb0
#    print(numb%10)
#    numb=numb10


#Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа
#n = int(input())
#sum = 0
#while n0
#    sum+= n%10
#    n= n10
#print(sum)


#n = int(input())
#P = 1
#while n0
    #P= n%10
    #n= n10
#print(P)


#Программа принимает на вход одно натуральное число и выводит на экран
#минимальную и максимальную цифры данного числа в отдельных строчках
#x = int(input())
#min = max = x%10 #последний член и мин и макс
#while x0
#    if x%10max
#        max = x%10
#    if x%10min
#        min= x%10
#    x=x10
#print(f'{min}n{max}')


#Программа принимает на вход одно натуральное число.
#Ваша задачи найти сколько раз встречается цифра 7 в этом числе
#a = bin(int(input())) # получаем строку пример bin(18) = '0b10010'
#a = a[2] # убираем первые два символа, 0b - первый знак числа вроде, второй система счисления
#kol = len(a)
#a=int(a)
#while kol0
#    print(a%10)
#    a = a10
#    kol-=1


#number = int(input())
#i=1
#key = 0
#while i=number
#    if number%i == 0
#        key+=1
#    if key2
#        print('No')
#        break
#    i+=1
#if key==1
#    print('No')
#elif key==2
#    print('Yes')


#Программа получает на вход натуральное число N.
#Нужно найти сумму его делителей.
#number = int(input())
#i=1
#sum = 0
#while i=number
#    if number%i==0
#        sum+=i
#    i+=1
#print(sum)


#a = int(input())
#b = int(input())
#while a!=b
#    if ab
#        a=a-b
#    else
#        b=b-a
#print(a)


#a,b =map(int, input().split())
#print(a+b)


#x = int(input())
#print(f'{int(x6)} {int(2x3)} {int(x6)}')


#x,y,z = map(int, input().split()) # ввели количество
#X - карандашей, Y - ручек, Z - фломастеров


#n = int(input())
#for i in range(n+1)
#    if i == 1 or i == 0
#        continue
#    else
#        if n%i == 0
#            print(i)
#            break


#a = int(input())
#b = int(input())
#while a=b
#    if a % 777 == 0
#        break
#    else
#        if a % 2 == 0 or a % 3 == 0
#            pass
#        else
#            print(a)
#    a+=1


#Сиракузская последовательность, или последовательность Коллатца, строится так
# возьмём натуральное число n; если оно чётное, то заменим его числом n2; если же оно нечётное, то заменим его числом 3n+1.
# Получившееся число — следующее в сиракузской последовательности после числа n.
# Затем заменяем получившееся число по тому же правилу, и так далее.
#Определите, сколько шагов потребуется сиракузской последовательности, стартующей с заданного числа, чтобы прийти к 1.
#n = int(input())
#k=0
#while n!=1
#    if n%2==0
#        n=2
#        k+=1
#    else
#        n=3n+1
#        k+=1
#print(k)


#letter = input()
#k = len(letter)
#end_marker = len(letter)
#counter=0
#i = 0
#while k!=0
#    if letter[i]==e or letter[i]=='a'
#        print('Ага! Нашлась')
#        break
#    print(f'Текущая буква {letter[i]}')
#    counter+=1
#    letter = letter[11]
#    k-=1
#if counter==end_marker
#    print('Распечатали все буквы')


#my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
#N = len(my_list)
#for i in range(N - 1)
#    for j in range(N - i - 1)
#        if my_list[j]  my_list[j + 1]
#            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#print(my_list[0], my_list[-1])

#new_list = sorted(my_list)
#print(new_list[0], new_list[-1])


#flag = False
#my_list = list(map(int,input().split()))
#for i in my_list
#    if i == 777
#        flag = True
#if flag == False
#    print('False')
#else
#    print('True')


#my_list = list(map(int, input().split()))
#sum = 0
#for i in my_list
#    sum+=i
#print(sum)


#mass = list(map(int,input().split()))
#N = len(mass)
#for i in range(N-1)
#    for j in range(N - i - 1)
#        if mass[j]  mass[j + 1]
#                mass[j], mass[j + 1] = mass[j + 1], mass[j]
#print(mass[0],mass[-1])


#list_numbers = list(map(int, input().split()))
#Summ = 0
#k=0
#for i in list_numbers
#    Summ+=i
#    k+=1
#print(Summk)


#first_hour = int(input())
#first_min = int(input())
#first_sec = int(input())
#second_hour = int(input())
#second_min = int(input())
#second_sec = int(input())
#delta_hour_to_sec = (second_hour-first_hour)3600
#delta_min_to_sec = (second_min-first_min)60
#summa = delta_hour_to_sec + delta_min_to_sec + (first_sec+second_sec)
#print(summa)


#a,b = map(int, input().split())
#print(abs(a)+abs(b))


#list_number = list(map(int, input().split()))
#s = sorted(list_number)
#print(s[-1])


#number = int(input())
#print((number-1),(number),(number+1),sep='')


#separator = input()
#for i in range(1,6,1)
    #print(i,end=separator)


#print('Гвидо', 'Ван', 'Россум', sep='', end='-')
#print('Основатель', 'Питона', sep='_', end='!')


#n = int(input())
#a = n  100
#b = n  10 % 10
#c = n % 10
#print(a,b,c,sep=',')


#n = int(input())
#boys = list(map(int, input().split()))
#
#m = int(input())
#girls = list(map(int, input().split()))
#
#k_boys=0
#k_girls=0
#boys.sort()
#girls.sort()
#print(boys,girls)
#i = 0
#j = 0
#count=0
#while i  n and j  m
#    if abs(boys[i] - girls[j]) = 1
#        count+=1
#        i+=1
#        j+=1
#    elif boys[i]girls[j]
#        i+=1
#    else
#        j+=1
#print(count)


#n = int(input())
#key_two = 0
#key_one = 0
#for i in range(n):
#    score_one,score_two = map(int,input().split())
#    if score_one>=score_two:
#        key_one+=1
#    else:
#        key_two+=1
#if key_one==key_two:
#    print('Friendship is magic!^^')
#elif key_one>key_two:
#   print('Mishka')
#else:
#    print('Chris')


#n = int(input())#количество строк для ввода
#for index,value in enumerate(range(1,n+1,1)):
#    value = input()
#    print(f'{index} строка, значение равно {value}')


#n = int(input())
#a = []
#for i in range(0,n):
#    s = input()
#    if 'соль' not in s:
#        a.append(s)
#print(', '.join(a))


#n = int(input())
#s = 0
#for i in range(n):
#    if i%3==0 or i%5==0:
#        s+=i
#print(s)


#s=0
#for i in range(50,101,1):
#    s+=i**3
#print(s)


#n = int(input())
#for i in range(n):
#    word = input().lower()
#    if 'рок' in word:
#        print(i+1,int(word.find('рок')+1))


#n = int(input())
#for i in range(n):
#    s = input()
#    if len(s)>10:
#        print(s[0]+str(len(s)-2)+s[-1])
#    else:
#        print(s)


#a,b = map(int,input().split())
#print(a%7==0 and b%7==0)


#a,b,c = map(int, input().split())
#print((a**2)+(b**2) == (c**2))


#list_one = list(map(int, input().split()))
#new_list = sorted(list_one)
#the_First_member, the_Second_member, the_Third_member =  new_list[0], new_list[1], new_list[2]
#print((the_First_member**2)+(the_Second_member**2)==(the_Third_member**2))


#n = int(input())#количество строк
#new_list = []
#for i in range(n):
#    new_value = input()
#    new_list.append(new_value)
#print(new_list)


#string_one = input() #буква
#string_two = input() # фраза
#summ = string_two.split()
#for i in summ:
#    if string_one in i:
#        print(i)


#some_list = list(map(int,input().split()))
#k = 0 # cколько положительных в списке
#flag = True
#for i in some_list:
#    if i>0:
#        min = i
#        break # нашли положительынй и вышли
#    else:
#        k+=1
#if k==len(some_list):
#    print('Empty')
#else:
#    for i in some_list:
#        if i<min and i>0:
#            min = i
#    print(min)


#string  = input().lower()
#kol_Of_Max=0
#for i in string:
#    considered_literally = i
#    k_of_considered_literally = 0
#    for j in string:
#        if i==j:
#            k_of_considered_literally+=1
#    if k_of_considered_literally>kol_Of_Max:
#        kol_Of_Max = k_of_considered_literally
#print(kol_Of_Max)



#пусть k - счетчик, по нему будем определять четное и нечетное место :)
#number = input() # ввели строку
#k = 1
#sum_chetn = 0
#sum_nechet = 0
#for i in number:
#    if k%2==0: # если четное число, то делится нацело на 2 без остатка
#        sum_chetn+=int(i)
#    else:
#        sum_nechet+=int(i)
#    k+=1
#if (sum_nechet - sum_chetn)%11==0:
#    print('YES')
#else:
#    print('NO')


#string = input()
#k = 0
#sum = 0
#for i in string:
#    if i.isdigit()==True:
#        k+=1
#        sum+=int(i)
#print(f'{k} {sum}')


#string = input()
#flag = True
#while flag == True and len(string)!=1:
#    if string[0]==string[-1]:
#        string = string[1:-1:1]
#    else:
#        flag = False
#if flag == False:
#    print('NO')
#else:
#    print('YES')


# 89 45 7 33 65 12
#a = list(map(int, input().split()))
#b = a[-1:-4:-1]
#a = b[::-1]
#print(a)


#top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
#for index, value in enumerate(top):
#    if value == 'Бригада':
#        top[index] = 'Друзья'
#    if value == 'Cверхъестественное':
#        top[index] = 'Настоящий детектив'
#print(top)


#mas = input().split()
#mas.reverse()
#print(mas)


#a = list(map(int, input().split()))
#print(a.count(999))


#string = (input().upper()).split()
#first_list, second_list = list(string[0]), list(string[1])
#end_first = '-'.join(first_list)
#end_second = '-'.join(second_list)
#print(end_first + ' ' + end_second)


#string = list(input().split())
#string = '\n'.join(string)
#print(string)


#string = list(input().split())
#name = string[1]
#family = string[2]
#first_letter_of_name = list(name)[0]
#first_letter_of_family = list(family)[0]
#print(f'{string[0]} {first_letter_of_name}. {first_letter_of_family}.')

#def summa(num):
#    sum = 0
#    while (num != 0):
#        sum = sum + num % 10
#        num = num // 10
#    return(sum)
#second_summ = 0
#for num in range(1000,10000):
#    if summa(num)%20==0:
#        second_summ+=num
#print(second_summ)


#n = int(input())
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(j, end = ' ')
#    print()


#k = 0 # количество делителей
#count = 0 # количество
#n = int(input())
#for i in range(n,2*n+1):
#    for j in range(i,2i+1):
#        if i%j==0:
#            k+=1 #количество делителей
#    if k==2: # простое число делится только на себя и на 1
#       count+=1
#print(count)


#n = int(input())
#count = 0
#for p in range(n+1,2*n):
#    if p%2==0 and p!=2 or p==1:
#        continue
#    d = 3
#    is_plain = True
#    while d*d<=p:
#        if p%d == 0:
#            is_plain = False
#            break
#        d+=2
#    if is_plain:
#        count+=1
#print(count)


