#банкомат
import time
def bank():
    return print('вставте карту')
bank()
def pin(a):
    a=5872
    return a
def bal(x):
    return x
def nal(x,y):
    return x-y
time.sleep(2)
x=5000
c=3
b=0
y=0
while b<=2:
    a = int(input('введите пин:'))
    b+=1
    c-=1
    if pin(a)!=a:
        print('неверный пин:осталоссь ',c,'попыток')
        continue
    while True:
        if pin(a) == a:
            d = input('введите операцию:')
        if d=='снятие':
            y=int(input('введите сумму:'))
            if bal(x)<y:
                print('недостаточно средств')
            else:
                nal(x, y)
                print('выполнено')
        elif   d == 'баланс':
                print('ваш баланс состовляет', bal(x) - y, 'рублей')
        aa = input('желаете выбрать другую операцию:')
        if aa=='да':
            continue
        elif aa == 'нет':
            exit()