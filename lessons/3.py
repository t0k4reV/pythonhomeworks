arr = []
for i in range(3):
    arr.append(int(input()))
price = sum(arr)
if arr[1] > arr[0] and arr[2] > arr[1]:
    price /= 2
    print(f'Акция! Ваша покупка составила всего: {price} рубля')
elif arr[0] > arr[1] and arr[1] > arr[2]:
    price /= 3
    print(f'Акция! Ваша покупка составила всего: {price} рубля')
else:
    print(f"К оплате {price} рублей")
