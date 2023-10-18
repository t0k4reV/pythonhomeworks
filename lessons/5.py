num = int(input())
arr = list(str(num))
arr = [int(x) for x in arr]
if int(str(num)[-1]) % 2 == 0 and sum(arr) % 2:
    res = num / 6
    print(f'число делится на 6. Результат деления = {res}')

