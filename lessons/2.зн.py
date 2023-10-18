timenow = int(input('Введите время: '))
price = int(input('Введите сумму к оплате: '))
if timenow > 10 and timenow < 12:
    price /= 2
    print(price)
elif timenow > 20 and timenow < 22:
    price /= 4
    print(price)
else:
    print(f'Ваша сумма к оплате: {price}')
