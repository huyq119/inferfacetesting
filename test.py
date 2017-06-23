while True:
    y=input('请输入正整数: ')
    try:
        y=int(y)
    except:
        print('输入错误')
        continue
    else:
        if y>0:
            break
        else:
            print('输入错误')
            continue
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, '具有因子', x)
        break
    x -= 1
else:
    print(y, '是质数')
