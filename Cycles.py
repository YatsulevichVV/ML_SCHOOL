# Теория
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('Stop')

n = int(input())
while n != 0:
    n = int(input())
else:
    print('Stop')

lst = [1, 5, None, 'sdfsdf', 12312, 0.5]
for i in lst:
    print(i)

for i in range(5):
    print(i)

print(round(0.1231231, 3))

lst.append(5)

# Задача 1
n = int(input())
i = 0
acc = 0
while i < n:
    ai = int(input())
    acc = acc + ai
    i = i + 1
print(round(acc / n, 3))


# Задача 2
a = int(input())
lst = []
while a != 0:
    lst.append(a)
    a = int(input())
else:
    n = int(input())
    print(lst[n])

# Задача 3
n = int(input())
y_true = []
y_pred = []
for i in range(n):
    a = int(input())
    y_true.append(a)
for i in range(n):
    a = int(input())
    y_pred.append(a)
acc = 0
for i in range(n):
    d = abs(y_true[i] - y_pred[i])
    acc += d
print(acc / n)

