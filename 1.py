maxsize, users = map(int, input().split())
arr = []
size = 0
summ = 0
swapped = True
x = -1
t = 0
for i in range(users):
    size = int(input())
    arr.append(size)
while swapped:
    swapped = False
    x += 1
    for i in range(1, users - x):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            swapped = True
for i in range(0, users):
    summ += arr[i]
    if summ > maxsize:
        summ -= arr[i]
        break
print(summ)


        
    
    
            
            
    